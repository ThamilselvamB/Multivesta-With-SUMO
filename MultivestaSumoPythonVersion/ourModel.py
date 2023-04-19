import random
from sumo_runner import SumoSimulation
simTime = 0

class ourModelClass:
 sr = SumoSimulation()


 def __init__(self):
  
  simTime = 0
  
 	
 def getTime(self):
  global simTime
  return simTime
  
 def oneStep(self):
    sr.one_step()

 def setSimulatorForNewSimulation(self,random_seed):
    sr.set_simulator_for_new_simulation(random_seed)
	
 def eval(self,obs):
  print("evaluation is called at ",simTime )
  if obs=="timeStep":
   return self.getTime()
  if obs=="st":
   #self.oneStep()
   return sr._collect_waiting_times("T1")
   #return random.randint(1,10)
  else:
   return 0


