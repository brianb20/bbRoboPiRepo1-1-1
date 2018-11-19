import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys
import time

RPL.servoWrite(0, 1500)
RPL.servoWrite(1, 1500)
