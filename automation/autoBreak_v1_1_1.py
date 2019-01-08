import RoboPiLib as RPL
import sys
import time
import MoveBase_v1_1_1 as MvB
RPL.RoboPiInit("/dev/ttyAMA0",115200)

sensor_pin_1 = 16
sensor_pin_2 = 17
RPL.pinMode(sensor_pin_1, RPL.INPUT)
RPL.pinMode(sensor_pin_2, RPL.INPUT)

ticksDone = 0
tickslimit = 200

while ticksDone < ticksLimit:
