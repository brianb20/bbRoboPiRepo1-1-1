import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys
import time

RPL.servoWrite(0, 2000)
RPL.servoWrite(1, 1000)

print("Snoozing...")
time.sleep(30)
print("Ok we done")

RPL.servoWrite(0, 1500)
RPL.servoWrite(1, 1500)
RPL.servoWrite(0, 0)
RPL.servoWrite(1, 0)

