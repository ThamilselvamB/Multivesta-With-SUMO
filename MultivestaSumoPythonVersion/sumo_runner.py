from __future__ import absolute_import
from __future__ import print_function

import sys
import numpy as np
import random
import timeit
import time
import os

sys.path.append(os.path.join(os.environ.get("SUMO_HOME"), 'tools'))
import traci
from sumolib import checkBinary
from generator import TrafficGenerator

traffic_jun_name = {"T1":"B2","T2":"C2","T3":"D2","T4":"B1","T5":"C1","T6":"D1"}
# detector_100 = get_detectors('../intersection/in/add/my_grid_detector_100.add.xml')
# detector_400 = get_detectors('../intersection/in/add/my_grid_detector_400.add.xml')
#traffic_juns = ["T1","T2","T3","T4","T5","T6"]
traffic_juns = ["T1"]
phases = ["P1","P2","P3","P4"]  
incoming_edges = {"T1":['B3B2','C2B2','B1B2','A2B2'],"T2":['C3C2','D2C2','C1C2','B2C2'],"T3":['D3D2','E2D2','D1D2','C2D2'],
                  "T4":['B2B1','C1B1','B0B1','A1B1'],"T5":['C2C1','D1C1','C0C1','B1C1'],"T6":['D2D1','E1D1','D0D1','C1D1']}
                  
walking_areas = {
                 "T1":[':B2_w0',':B2_w1',':B2_w2',':B2_w3'],
                 "T2":[':C2_w0',':C2_w1',':C2_w2',':C2_w3'],
                 "T3":[':D2_w0',':D2_w1',':D2_w2',':D2_w3'],
                 "T4":[':B1_w0',':B1_w1',':B1_w2',':B1_w3'],
                 "T5":[':C1_w0',':C1_w1',':C1_w2',':C1_w3'],
                 "T6":[':D1_w0',':D1_w1',':D1_w2',':D1_w3']
}

print("Oom Namasivaya")
class SumoSimulation:
    #route_gen = TrafficGenerator(300,300)
    
    def __init__(self) -> None:
        self._waiting_times = {'T1':{},'T2':{},'T3':{},'T4':{},'T5':{},'T6':{}}
        self.sumo_cmd = self.set_sumo(False, 'sumo_grid_config.sumocfg', 3000)
        self.step = 0
        traci.start(self.sumo_cmd)
        

    def set_sumo(self, gui, sumocfg_file_name, max_steps):
        """
        Configure various parameters of SUMO
        """
        # sumo things - we need to import python modules from the $SUMO_HOME/tools directory
        if 'SUMO_HOME' in os.environ:
            tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
            sys.path.append(tools)
        else:
            sys.exit("please declare environment variable 'SUMO_HOME'")

        # setting the cmd mode or the visual mode    
        if gui == False:
            sumoBinary = checkBinary('sumo')
        else:
            sumoBinary = checkBinary('sumo-gui')

        # setting the cmd command to run sumo at simulation time
        sumo_cmd = [sumoBinary, "-c", os.path.join('intersection', sumocfg_file_name), "--no-step-log", "true", "--waiting-time-memory", str(max_steps)]
        return sumo_cmd
    

    def set_simulator_for_new_simulation(self, random_number):
        traci.close()
        self.step = 0
        #TrafficGenerator.check()
        TrafficGenerator.generate_routefile(300,random_number)
        time.sleep(3)
        print("Routes are generated -----------------------", random_number)
        #sumo_cmd = self.set_sumo(False, 'sumo_grid_config.sumocfg', 3000)
        traci.start(self.sumo_cmd)
        

    def one_step(self):
        if self.step < 300:
            traci.simulationStep()  # simulate 1 step in sumo
            #print("simulation is running")
            self.step += 1
        else:
            print("simulation is completed")
           
    def get_is_simulation_finished(self):
        print("get_is_simulation_finished is called in testing simulation part......")
        if self._step >= 300:
           return True
        return False
    
    def eval(self,obs):
    
        if obs=="timeStep":
            return self.step
            
        if obs=="st":
            return self._collect_waiting_times("T1")
        else:
            return 0
        
    def _calculate_pedestrian_waiting_time(self,walking_edges,for_whom,debug,info):
        cumulative__waiting_time = []
        no_of_pedestrian_waiting = 0
        for edge in walking_edges:
            peds = traci.edge.getLastStepPersonIDs(edge)
            for ped in peds:
                wt = traci.person.getWaitingTime(ped)
                if wt > 0:
                    no_of_pedestrian_waiting += 1
                cumulative__waiting_time.append(wt)
                if debug:
                    print("Pedestrian %s waiting at edge %s for %s steps"%(ped,edge,wt))
        if for_whom == "STATE":
            if info:
                print("Numbero of Pedestrians Waiting: ", no_of_pedestrian_waiting)
            return no_of_pedestrian_waiting
        else:
            if info:
                print("Cumulative Pedestrian Waiting Time: ", cumulative__waiting_time)
            return sum(cumulative__waiting_time)

    def _collect_waiting_times(self, intersection):
        # ''' 'B3B2','C2B2','B1B2','A2B2' '''
        halt_N = traci.edge.getLastStepHaltingNumber("B3B2")
        halt_S = traci.edge.getLastStepHaltingNumber("C2B2")
        halt_E = traci.edge.getLastStepHaltingNumber("B1B2")
        halt_W = traci.edge.getLastStepHaltingNumber("A2B2")
        queue_length = halt_N + halt_S + halt_E + halt_W
        print("queue length: ",queue_length)
        return queue_length 
     
    def _collect_waiting_times1(self, intersection):
        """
        Retrieve the waiting time of every car in the incoming roads
        """
        incoming_roads = incoming_edges[intersection]
        car_list = traci.vehicle.getIDList()
        for car_id in car_list:
            wait_time = traci.vehicle.getAccumulatedWaitingTime(car_id)
            road_id = traci.vehicle.getRoadID(car_id)  # get the road id where the car is located
            if road_id in incoming_roads:  # consider only the waiting times of cars in incoming roads
                self._waiting_times[intersection][car_id] = wait_time
            else:
                if car_id in self._waiting_times[intersection]: # a car that was tracked has cleared the intersection
                    del self._waiting_times[intersection][car_id] 
        pd_wt = self._calculate_pedestrian_waiting_time(walking_areas[intersection],"wait",False,False)
        total_waiting_time = sum(self._waiting_times[intersection].values()) + pd_wt
        print("WT: ",sum(self._waiting_times[intersection].values()),"PDWT: ",pd_wt)
        return total_waiting_time

'''
SumoSimulation = SumoSimulation()
start_time = timeit.default_timer()
_step = 0
while _step < 100:
    traci.simulationStep()  # simulate 1 step in sumo
    #print("Hi")
    print("WT: ",SumoSimulation._collect_waiting_times('T1'))
    _step += 1 # update the step counter

traci.close()
simulation_time = round(timeit.default_timer() - start_time, 1)
'''