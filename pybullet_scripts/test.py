import pybullet as p

p.connect(p.GUI)
robot_id = p.loadURDF("../urdf/vector.urdf", useFixedBase=True)