import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys
import time

print("32.2.2.1")
print("...")
RPL.servoWrite(0, 2000)
time.sleep(0.25)
print("---")
print("32.2.2.2")
print("...")
RPL.servoWrite(0, 1600)
time.sleep(0.25)
print("---")
print("32.2.2.3")
RPL.RoboPiExit() #This disables the motors entirely.
time.sleep(0.25)
print("---")
print("32.2.2.4")
print("...")
RPL.servoWrite(0, 1000)
time.sleep(0.25)
print("---")
print("32.2.2.5")
print("...")
RPL.servoWrite(0, 1400)
time.sleep(0.25)
print("---")
print("32.2.2.6")
print("...")
RPL.servoWrite(0, 1500) #This halts moter movement but the motor is still on.
time.sleep(0.25)
