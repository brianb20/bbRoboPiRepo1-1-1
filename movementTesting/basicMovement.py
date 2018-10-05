import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys

mtrLeft = 0
mtrRight = 1

runLoop1 = True
runLoop2 = False

try:
  RPL.pinMode(motorL,RPL.SERVO)
  RPL.servoWrite(motorL,1500)
  RPL.pinMode(motorR,RPL.SERVO)
  RPL.servoWrite(motorR,1500)
except:
pass

while runLoop1 == True:
    print("---===MOMENTUM ROBOT CONTROL===---")
    print("Chose your control type:")
    print("1 - Standard WASD")
    i1 = input()
    if int(i1) == 1:
        runLoop1 = False
        runLoop2 = True
        print("Running...)
    else:
        print("Invalid input. Please enter a correct input."")
    #print("2 - Tank mode - ")

def motorMove(dir1, dir2):
    if dir1 != 0:
        if dir2 != 0: #Both motors
            print("Moving both motors")
            RPL.servoWrite(mtrLeft, dir1)
            RPL.servoWrite(mtrRight, dir2)
        else: #Left motor
            print("Moving left motor")
            RPL.servoWrite(mtrLeft, dir1)
            RPL.servoWrite(mtrRight, 1500)
    else if dir2 != 0: #Right motor
        print("Moving right motor")
        RPL.servoWrite(mtrLeft, 1500)
        RPL.servoWrite(mtrRight, dir2)
    else:
        RPL.servoWrite(mtrLeft, 1500)
        RPL.servoWrite(mtrRight, 1500)

while runLoop2 == True:
    input = sys.stdin.read(1) #jacked from resource;
    if input == "w":
        motorMove(2000, 2000)
    if input == "a":
        motorMove(0, 2000)
    if input == "s":
        motorMove(1000, 1000)
    if input == "d":
        motorMove(2000, 0)
    if input == "x":
        motorMove(0, 0)
        runLoop2 == False:
