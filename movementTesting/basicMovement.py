import roboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys, tty, termios, signal, time

mtrLeft = [0, 1]
mtrRight = [1, -1]

mtrLeftMove = 1500
mtrRightMove = 1500

runLoop1 = True
runLoop2 = False

#try:
#	RPL.pinMode(mtrLeft[0],RPL.SERVO)
#	RPL.servoWrite(mtrLeft[0],1500)
#	RPL.pinMode(mtrRight[0],RPL.SERVO)
#	RPL.servoWrite(mtrRight[0],1500)
#except:
#	pass

def clearText():
	_ = system('clear')

def motorMove(mot1, mot2):
	print("Help!")
	mtrLeftMove = float(1500 + ((float(mtrLeft[1]) * (float(mot1) / 100) * 500)))
	mtrRightMove = float(1500 + ((float(mtrRight[1]) * (float(mot2) / 100) * 500)))
	RPL.servoWrite(mtrLeft[0], mtrLeftMove)
	RPL.servoWrite(mtrRight[0], mtrRightMove)

def interrupted(signum, frame): #copied from resource
        motorMove(0, 0)

signal.signal(signal.SIGALRM, interrupted) #copied from resource
tty.setraw(sys.stdin.fileno()) #copied from resource

SHORT_TIMEOUT = 0.255 #copied from resource

while runLoop1 == True:
	print("---===MOMENTUM ROBOT CONTROL===---")
	print("1 - Configure")
	print("2 - Control")
	i1 = input()
	if int(i1) == 1:
		runLoop2 = True
	elif int(i1) == 2:
		runLoop3 = True
	else:
		print("Invalid input. Please enter a correct input.")
	
	while runLoop2 == True:
		clearText()
		print("--==CONFIGURE INPUTS==--")
		print("Motor 1 Socket ID: " + str(mtrLeft[0]))
		if mtrLeft[1] == 1:
			print("Motor 1 Forward Direction: Forward")
		else:
			print("Motor 1 Forward Direction: Backward")
		print("-----")
		print("Motor 2 Socet ID: " + str(mtrRight[0]))
		if mtrRight[1] == 1:
			print("Motor 2 Forward Direction: Forward")
		else:
			print("Motor 2 Forward Direction: Backward")
		print("-----")
		print("1 - Change Motor 1 Socket ID")
		print("2 - Invert Motor 1 Rotation")
		print("3 - Change Motor 2 Socket ID")
		print("4 - Invert Motor 2 Rotation")
		print("0 - Back to Main Menu")
		i2 = input()
		if int(i2) == 1:
			i3 = input("Input new Motor 1 Socket ID: ")
			mtrLeft[0] = int(i3)
			print("Motor 1 Socket ID changed to " + str(i3))
			time.sleep(8)
		elif int(i2) == 2:
			mtrLeft[1] = mtrLeft[1] * -1
			time.sleep(8)
		elif int(i2) == 3:
			i4 = input("Input new Motor 2 Socket ID: ")
			mtrRight[0] = int(i4)
			print("Motor 2 Socket ID changed to " + str(i4))
			time.sleep(8)
		elif int(i2) == 4:
			mtrRight[1] = mtrRight[1] * -1
			time.sleep(8)
		elif int(i2) == 0:
			runLoop2 = False
		else:
			print("Invalid input. Please enter a correct input.")
			time.sleep(8)

	while runLoop3 == True:
		clearText()
		print("--==CHOSE CONTROL SCHEME==--")
		print("1 - WASD - Standard WASD controls; no multi-key input (YET).")
		print("0 - Back to Main Menu")
		i3 = input()
		if int(i3) == 1:
			runLoop4 = True
		if int(i3) == 0:
			runLoop3 = False
		else:
			print("Invalid input. Please enter a correct input.")
			time.sleep(8)

	while runLoop4 == True:
		signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) #copied from resource
		input = sys.stdin.read(1) #copied from resource;
		signal.setitimer(signal.ITIMER_REAL, 0) #copied from resource;
		if input == "w":
			motorMove(100, 100)
		elif input == "a":
			motorMove(0, 100)
		elif input == "s":
			motorMove(100, 0)
		elif input == "d":
			motorMove(-100, -100)
		elif input == "x":
			motorMove(0, 0)
			runLoop4 = False
