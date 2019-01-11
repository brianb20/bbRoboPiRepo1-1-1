import RoboPiLib as RPL

import sys
import time
import MoveBase_v1_1_1 as MvB
RPL.RoboPiInit("/dev/ttyAMA0",115200)

sensor_pin_1 = 23 #18
sensor_pin_2 = 17
RPL.pinMode(sensor_pin_1, RPL.INPUT)
RPL.pinMode(sensor_pin_2, RPL.INPUT)

ticksDone = 0
ticksLimit = 300
ticksActive = 0
ticksInactive = 0
sensor1Active = False
sensorTickThreshold = 2

while (ticksDone < ticksLimit):
	reading1 = RPL.digitalRead(sensor_pin_1)
	reading2 = RPL.digitalRead(sensor_pin_2)
	print("Sensor1: " + str(reading1) + ", Sensor2: " + str(reading2))
	if(reading1 == 0):
		sensor1Active = True
		ticksActive += 1
		ticksInactive = 0
	else:
		sensor1Active = False
		ticksInactive += 1
		if (ticksInactive > 3):
			ticksActive = 0

	if(ticksActive < sensorTickThreshold - 4):
		MvB.motorMove(50, 50)
	elif(ticksActive < sensorTickThreshold * 1.5):
		MvB.motorMove(25, 25)
	elif(ticksActive < sensorTickThreshold * 1.75):
		MvB.motorMove(15, 15)
	elif(ticksActive < sensorTickThreshold * 1.90):
		MvB.motorMove(5, 5)
	else:
		MvB.motorMove(0, 0)
	ticksDone += 1
	time.sleep(0.15)
MvB.allStop()
