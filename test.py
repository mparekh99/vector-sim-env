import pybullet as p
import pybullet_data
import time
import os
import math


physicsClient = p.connect(p.GUI) # or DIRECT for non ui
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally

p.setGravity(0, 0, -10)
planeID = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("/urdf/vector.urdf", cubeStartPos, cubeStartOrientation)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)  # 1 0ver 240th of a second 

cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)

p.disconnect()




