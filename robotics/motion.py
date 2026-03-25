from robodk.robolink import

#Connect to RoboDK
RDK = Robolink()

#Get robot
robot = RDK.Item('Cobot 1200', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("Robot not found")

#Get targets
home = RDK.Item('Home')
T1   = RDK.Item('T1')
T4   = RDK.Item('T4')

#Check that all targets exist
if not home.Valid() or not T1.Valid() or not T4.Valid():
    raise Exception("Check that Home, T1, or T4 targets are missing")

#Set speed
robot.setSpeed(100)       # linear speed mm/s
robot.setSpeedJoints(50)  # joint speed deg/s

#Move sequence
print("Moving to Home")
robot.MoveJ(home)

print("Moving to T1")
robot.MoveJ(T1)

print("Moving to T4")
robot.MoveJ(T4)

print("Returning to Home")
robot.MoveJ(home)

print("Movement completed")
RDK = Robolink()

#Get robot
robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("Robot not found")

#Get targets
home = RDK.Item('Home')
T1   = RDK.Item('T1')
T4   = RDK.Item('T4')

#Check that all targets exist
if not home.Valid() or not T1.Valid() or not T4.Valid():
    raise Exception("Check that Home, T1, or T4 targets are missing")

#Set speed
robot.setSpeed(100)       # linear speed mm/s
robot.setSpeedJoints(50)  # joint speed deg/s

#Move sequence
while True:
    print("Moving to Home")
    robot.MoveJ(home)
    print("Moving to T1")
    robot.MoveJ(T1)
    print("Moving to T4")
    robot.MoveJ(T4)
    print("Returning to Home")
    robot.MoveJ(home)
    print("Movement completed")

   

