import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys
import time

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
reading = RPL.digitalRead(sensor_pin)
ticks = 100000
ticksDone = 0
while ticks > 0:
	print("SensorInput " + str(ticksDone) + "|" + str(ticks) + ": " + str(RPL.digitalRead(sensor_pin)))
	ticks -= 1
	ticksDone += 1
	print(".")
	if RPL.digitalRead(sensor_pin) == 1:
		RPL.servoWrite(0, 1500)
		RPL.servoWrite(0, 0)
		RPL.servoWrite(1, 1500)
		RPL.servoWrite(1, 0)
	else:
		RPL.servoWrite(0, 2000)
		RPL.servoWrite(1, 1000)
	print("..")
	time.sleep(0.5)
	print("...")
