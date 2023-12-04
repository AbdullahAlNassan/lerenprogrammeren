from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Stapels oppakken, verplaatsen en neerzetten
for i in range(4):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for j in range(4):
        robotArm.moveLeft()

for _ in range(3): robotArm.moveLeft()

for i in range(3):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for j in range(4):
        robotArm.moveLeft()

for _ in range(2): robotArm.moveLeft()

for i in range(2):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for j in range(4):
        robotArm.moveLeft()

robotArm.moveLeft()
robotArm.grab()
for j in range(5):
    robotArm.moveRight()
    robotArm.drop()


robotArm.wait()

