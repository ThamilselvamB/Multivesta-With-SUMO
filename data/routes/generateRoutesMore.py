from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import subprocess
import random
#  "518.38,517.78 501.38,517.78"
# we need to import python modules from the directory
sys.path.append(os.path.join('c:', os.sep, 'usr', 'share', 'sumo', 'tools'))
from sumolib import checkBinary  # import library
import traci
import numpy as np


class Configuration:
    def __init__(self, cases):
        start = 1
        end = 25
        # majorRoad = 1500
        # minorRoad = 750
        # leftTurn = 100
        # crossRoad = 600

        self.cases=cases
        self.tcH = {}
        self.routeH = {}
        self.pH = {}
        if cases == "Case1Low":
            multiplier = 1.0
            route_1_AmpliToVaishnamdevi = 22
            route_2AmpliToVaishnamdevi = 18
            route_3GandhinagarToShrikaei = 16
            route_4GandhinagarToShrikaei = 18
            route_5NavaNarodatoZundal = 19
            route_6NavaNarodatoZundal = 10
            route_7CGRoadtoUshmanpura = 10
            route_8CGRoadtoUshmanpura = 15
            route_9CGRoadtoUshmanpura = 16
            route_10CGRoadtoUshmanpura = 10
            route_11CGRoadtoUshmanpura = 17
            route_12CGRoadtoUshmanpura = 17
            route_13CGRoadtoUshmanpura = 17
            route_14CGRoadtoUshmanpura = 11
            route_15CGRoadtoUshmanpura = 16
            route_16CGRoadtoUshmanpura = 16
            route_17CGRoadtoUshmanpura = 10
            route_18CGRoadtoUshmanpura = 10
            route_19CGRoadtoUshmanpura = 112
            route_20CGRoadtoUshmanpura = 112
            route_21CGRoadtoUshmanpura = 123
            route_22CGRoadtoUshmanpura = 123
            route_23CGRoadtoUshmanpura = 129
            route_24CGRoadtoUshmanpura = 129
            route_25CGRoadtoUshmanpura = 186
            route_26CGRoadtoUshmanpura = 186

            crossRoad = 300
        if cases == "Case1Mid":
            multiplier = 1.0
            route_1_AmpliToVaishnamdevi = 200
            route_2AmpliToVaishnamdevi = 200
            route_3GandhinagarToShrikaei = 280
            route_4GandhinagarToShrikaei = 320
            route_5NavaNarodatoZundal = 200
            route_6NavaNarodatoZundal = 120
            route_7CGRoadtoUshmanpura = 175
            route_8CGRoadtoUshmanpura = 185
            route_9CGRoadtoUshmanpura = 180
            route_10CGRoadtoUshmanpura = 180
            route_11CGRoadtoUshmanpura = 200
            route_12CGRoadtoUshmanpura = 230
            route_13CGRoadtoUshmanpura = 91
            route_14CGRoadtoUshmanpura = 91
            route_15CGRoadtoUshmanpura = 81
            route_16CGRoadtoUshmanpura = 81
            route_17CGRoadtoUshmanpura = 75
            route_18CGRoadtoUshmanpura = 75
            route_19CGRoadtoUshmanpura = 912
            route_20CGRoadtoUshmanpura = 912
            route_21CGRoadtoUshmanpura = 1923
            route_22CGRoadtoUshmanpura = 1923
            route_23CGRoadtoUshmanpura = 1229
            route_24CGRoadtoUshmanpura = 1229
            route_25CGRoadtoUshmanpura = 816
            route_26CGRoadtoUshmanpura = 816
        if cases == "Case1High":
            multiplier = 1.0
            route_1_AmpliToVaishnamdevi = 999
            route_2AmpliToVaishnamdevi = 999
            route_3GandhinagarToShrikaei = 1156
            route_4GandhinagarToShrikaei = 1156
            route_5NavaNarodatoZundal = 912
            route_6NavaNarodatoZundal = 912
            route_7CGRoadtoUshmanpura = 1375
            route_8CGRoadtoUshmanpura = 1375
            route_9CGRoadtoUshmanpura = 912
            route_10CGRoadtoUshmanpura = 912
            route_11CGRoadtoUshmanpura = 912
            route_12CGRoadtoUshmanpura = 912
            route_13CGRoadtoUshmanpura = 912
            route_14CGRoadtoUshmanpura = 912
            route_15CGRoadtoUshmanpura = 816
            route_16CGRoadtoUshmanpura = 816
            route_17CGRoadtoUshmanpura = 750
            route_18CGRoadtoUshmanpura = 750
            route_19CGRoadtoUshmanpura = 912
            route_20CGRoadtoUshmanpura = 912
            route_21CGRoadtoUshmanpura = 1923
            route_22CGRoadtoUshmanpura = 1923
            route_23CGRoadtoUshmanpura = 1229
            route_24CGRoadtoUshmanpura = 1229
            route_25CGRoadtoUshmanpura = 816
            route_26CGRoadtoUshmanpura = 816
        if cases == "Case2":
            multiplier = 1.0
            majorRoad = 1600
            minorRoad = 1000
            leftTurn = 100
            crossRoad = 300
        if cases == "Case3":
            multiplier = 1.0
            majorRoad = 850
            minorRoad = 850
            leftTurn = 100
            crossRoad = 300
        if cases == "Case4":
            multiplier = 1.0
            majorRoad = 450
            minorRoad = 750
            leftTurn = 100
            crossRoad = 300

        self.pH1 = np.ones(1)*multiplier * route_1_AmpliToVaishnamdevi / 3600
        self.pH2 = np.ones(1) * multiplier * route_2AmpliToVaishnamdevi / 3600
        self.pH3 = np.ones(1) * multiplier * route_3GandhinagarToShrikaei / 3600
        self.pH4 = np.ones(1) * multiplier * route_4GandhinagarToShrikaei / 3600
        self.pH5 = np.ones(1) * multiplier * route_5NavaNarodatoZundal / 3600
        self.pH6 = np.ones(1) * multiplier * route_6NavaNarodatoZundal / 3600
        self.pH7 = np.ones(1) * multiplier * route_7CGRoadtoUshmanpura / 3600
        self.pH8 = np.ones(1) * multiplier * route_8CGRoadtoUshmanpura / 3600
        self.pH9 = np.ones(1) * multiplier * route_9CGRoadtoUshmanpura / 3600
        self.pH10 = np.ones(1) * multiplier * route_10CGRoadtoUshmanpura / 3600
        self.pH11 = np.ones(1) * multiplier * route_11CGRoadtoUshmanpura / 3600
        self.pH12 = np.ones(1) * multiplier * route_12CGRoadtoUshmanpura / 3600
        self.pH13 = np.ones(1) * multiplier * route_13CGRoadtoUshmanpura / 3600
        self.pH14 = np.ones(1) * multiplier * route_14CGRoadtoUshmanpura / 3600
        self.pH15 = np.ones(1) * multiplier * route_15CGRoadtoUshmanpura / 3600
        self.pH16 = np.ones(1) * multiplier * route_16CGRoadtoUshmanpura / 3600
        self.pH17 = np.ones(1) * multiplier * route_17CGRoadtoUshmanpura / 3600
        self.pH18 = np.ones(1) * multiplier * route_18CGRoadtoUshmanpura / 3600
        self.pH19 = np.ones(1) * multiplier * route_19CGRoadtoUshmanpura / 3600
        self.pH20 = np.ones(1) * multiplier * route_20CGRoadtoUshmanpura / 3600
        self.pH21 = np.ones(1) * multiplier * route_21CGRoadtoUshmanpura / 3600
        self.pH22 = np.ones(1) * multiplier * route_22CGRoadtoUshmanpura / 3600
        self.pH23 = np.ones(1) * multiplier * route_23CGRoadtoUshmanpura / 3600
        self.pH24 = np.ones(1) * multiplier * route_24CGRoadtoUshmanpura / 3600
        self.pH25 = np.ones(1) * multiplier * route_25CGRoadtoUshmanpura / 3600
        self.pH26 = np.ones(1) * multiplier * route_26CGRoadtoUshmanpura / 3600
        self.pH27 = np.ones(1) * multiplier * route_26CGRoadtoUshmanpura / 3600

        self.pH = np.hstack((self.pH1 , self. pH2,self.pH3,self.pH4,self.pH5 , self. pH6,self.pH7,self.pH8,self.pH9 , self. pH10,self.pH11,self.pH12,self.pH13 , self. pH14,self.pH15,self.pH16,
                             self.pH17, self.pH18, self.pH19, self.pH20,self.pH21 , self. pH22,self.pH23,self.pH24,self.pH25 , self. pH26,self.pH27))
        self.routeH = []
        for i in range(start,end):
            self.routeH.append("route_"+str(i) )
        # self.routeH = ["route_1","route_2","route_3","route_4","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1",
        #                "route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1"]

        # self.directions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15','16','17','18','19','20','1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A', '12A','13A','14A','15A','16A','17A','18A','19A','20A']
        # self.nrDirections = len(self.directions)
#<route id="route_1" edges="168277061#0 168277061#1 168277061#3 168277061#4 168275829 168275547#1 168275547#2 547236215#0 547236215#2 547236215#4 547236215#5 168278390#0 168278390#1 168278390#2 168278390#3 168278390#4 547560317 168278394 168278393#1 168278393#2 168274448#1 168244316#0 168244316#1 168244316#3 168244316#4 168244316#5 168244316#6 168108873#2"/>

#  Wiedemann  Krauss  IDM   

def generate_routefile(cases, outputfile,randomSeed):
    random.seed(random.randint(0,99))  # make tests reproducible
    N = 400  # number of time steps
    cf1 = Configuration("Case1Low")
    cf2 = Configuration("Case1Mid")
    cf3 = Configuration("Case1High")
    # according to distribution in Ahmadabad city
    pBus = 2. / 100
    pCar = 17. / 100
    p3Wheel = 6. / 100
    p2Wheel = 75. / 100
    pBus1 = 0.2 / 100
    pCar1 = 1.7 / 100
    p3Wheel1 = 0.6 / 100
    p2Wheel1 = 7.5 / 100
    v_Types = ['Bus','Auto','MotorCycle','Car','emergency']
    with open(""+outputfile, "w") as routes:
        totalCars = 0;
        print("""<routes>
<vType id="Bus" accel="0.6" decel="3.5" sigma="0.5" length="10.1" minGap="1.0" maxSpeed="16.67" carFollowModel="Wiedemann" guiShape="bus" width="2.45" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0"/>
<vType id="Auto" accel="0.7" decel="4.5" sigma="0.5" length="2.6" minGap="0.3" maxSpeed="16" carFollowModel="Wiedemann" guiShape="passenger/sedan" width="1.25" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0" />
<vType id="MotorCycle" accel="0.9" decel="3.5" sigma="0.5" length="1.85" minGap="0.15"  carFollowModel="Wiedemann" maxSpeed="17" guiShape="motorcycle" width="0.7" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0"/>
<vType id="Car" accel="0.8" decel="4.5" sigma="0.5" length="3.6" minGap="0.5" maxSpeed="40" carFollowModel="Wiedemann" guiShape="passenger" width="1.5" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0"/>
<vType id="emergency" accel="2.8" decel="5.5" sigma="0.5" length="3.6" minGap="0.5" maxSpeed="120.6" carFollowModel="Wiedemann" guiShape="emergency" width="1.5" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0" vClass="emergency" speedFactor="1.9" jmDriveAfterRedTime="300" jmDriveAfterRedSpeed="5.56">
<param key="has.bluelight.device" value="true"/>
<param key="has.fcd.device" value="true"/> 
</vType>
<route id="route_0" edges="1i 52i gneE0 gneE2" />
<route id="route_1" edges="-gneE2 -gneE0 52o 2i 1o" />
        <route id="route_2" edges="4i 3o" />
        <route id="route_3" edges="3i 4o" />
        <route id="route_4" edges="-gneE1 gneE3" /> 
        <route id="route_5" edges="4i 1o" />
        <route id="route_6" edges="4i 2o 52i gneE0 gneE1" />
        <route id="route_7" edges="2i 4o" />
        <route id="route_8" edges="2i 3o" />
        <route id="route_9" edges="-gneE1 gneE3" />
        <route id="route_10" edges="3i 2o 52i gneE0 gneE3" />
        <route id="route_11" edges="3i 1o" />
        <route id="route_12" edges="-gneE1 -gneE0 52o 2i 4o" />
        <route id="route_13" edges="-gneE1 gneE2" />
        <route id="route_14" edges="-gneE2 gneE1" />
        <route id="route_15" edges="-gneE2 gneE3" />
        <route id="route_16" edges="-gneE3 -gneE0 52o 2i 3o" />
        <route id="route_17" edges="-gneE3 gneE2" />
        <route id="route_18" edges="gneE0 gneE3" />
        <route id="route_19" edges="gneE0 gneE1" />
        <route id="route_20" edges="1i 2o 52i gneE0 gneE2 -gneE4 gneE5" />
        <route id="route_21" edges="-gneE5 gneE4 -gneE2 -gneE0 52o 2i 1o" />
        <route id="route_22" edges="-gneE5 gneE4 -gneE2 -gneE0 52o 2i 3o" />
        <route id="route_23" edges="1i 2o 52i gneE0 gneE2 -gneE4 gneE7" />

	<route id="route_24" edges="gneE0"/>""",
              file=routes)
        lastVeh = 0
        vehNr = 0  # 3,6,20 ----- 2,10,21 -------- 5,16,22   ----- 7,12,23
        list1 = [3,6,20,2,10,21]
        for i in range(int(round(N))):
           emergencyRandom = random.sample(list1,1)
           if(i<50):
            cf = cf2;
            #print("configuration selected now cf1: at time",i)
           if(i>=50 and i<150):
            cf = cf2
            #print("configuration selected now cf2: at time",i)
           if(i>=150 and i<300):
            cf = cf2
           if(i>=300 and i<400):
            cf = cf2
           if(i==0):
                
                
                print('<vehicle id="%s_%i" type="emergency" route="%s" depart="%i" />' % (v_Types[4], vehNr, cf.routeH[emergencyRandom[0]], i),file=routes)
                print('<vehicle id="%s_%i" type="Bus" route="%s" depart="%i" />' % (v_Types[0], vehNr, cf.routeH[emergencyRandom[0]], i),file=routes)                
                print('<vehicle id="%s_%i" type="Car" route="%s" depart="%i" />' % (v_Types[3], vehNr, cf.routeH[random.randint(0,19)], i),file=routes)
                vehNr += 1
           else:
            for j in range(len(cf.routeH)):
                # d = cf.directions[j]
                k = random.uniform(0, 1)
                #print("-------------------------------------------------", k)
                if k < cf.pH[j]:
                    #print("-------------------------- %s <  %s  : True now at %s-----------------------"%( k,cf.pH[j], i))
                    #print("now:",cf.pH)
                    route = cf.routeH[j]
                    # cf.tcH[d] = cf.tcH[d] + 1
                    k = random.randint(0, 3)
                    # if k == 0:
                    if random.uniform(0, 1) < pBus:
                        print('<vehicle id="%s_%i" type="Bus" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),file=routes)
                        vehNr += 1
                    if random.uniform(0, 1) < p3Wheel:
                        print('<vehicle id="%s_%i" type="Auto" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    if random.uniform(0, 1) < p2Wheel:
                        print('<vehicle id="%s_%i" type="MotorCycle" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    if random.uniform(0, 1) < pCar:
                        print('<vehicle id="%s_%i" type="Car" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    # print('<vehicle id="%s_%i" type="Auto" route="%s" depart="%i" />' % (
                    #     route, vehNr, route, i), file=routes)
                    # vehNr += 1
                    lastVeh = i
                     
        '''              
        for i in range(int(round(N/2)),N):
            if(i>10):
             cf = cf1;
            else:
             cf = cf2;
            if(i==0):
                print('<vehicle id="%s_%i" type="Bus" route="%s" depart="%i" />' % (v_Types[4], vehNr, cf.routeH[random.randint(0, 18)], i),file=routes)
                vehNr += 1
            else:
             for j in range(len(cf.routeH)):
                # d = cf.directions[j]
                if random.uniform(0, 1) < cf.pH[j]:
                    route = cf.routeH[j]
                    # cf.tcH[d] = cf.tcH[d] + 1
                    k = random.randint(0, 3)
                    # if k == 0:
                    if random.uniform(0, 1) < pBus:
                        print('<vehicle id="%s_%i" type="Bus" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),file=routes)
                        vehNr += 1
                    if random.uniform(0, 1) < p3Wheel:
                        print('<vehicle id="%s_%i" type="Auto" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    if random.uniform(0, 1) < p2Wheel:
                        print('<vehicle id="%s_%i" type="MotorCycle" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    if random.uniform(0, 1) < pCar:
                        print('<vehicle id="%s_%i" type="Car" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    # print('<vehicle id="%s_%i" type="Auto" route="%s" depart="%i" />' % (
                    #     route, vehNr, route, i), file=routes)
                    # vehNr += 1
                    lastVeh = i         
        
        '''
        print('<!-- totalCars="%i -->' % (vehNr), file=routes)
        print('<!-- CarsPerDirection="%s -->' % (str(cf.tcH)), file=routes)
        print("</routes>", file=routes)
        # print(cf.tcH)
        print("Total cars Generated:",vehNr)
    routes.close()

def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--cases", type="string", dest="cases", default="Case1Mid")
    optParser.add_option("--output", type="string", dest="output", default="cross.rou.xml")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    for i in range(1,21):
     filename = "cross_"+str(i)+".rou.xml"
     generate_routefile(options.cases, filename,32)
    # generate_routefileSimple()
