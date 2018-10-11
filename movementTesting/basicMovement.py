import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys, tty, termios, signal

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

def interrupted(signum, frame): #copied from resource
	motorMove(0, 0)

def clearText():
	_ = system('clear')

while runLoop1 == True:
	print("---===MOMENTUM ROBOT CONTROL===---")
	print("Chose your control type:")
	print("1 - Standard WASD")
	i1 = input()
	if int(i1) == 1:
		runLoop1 = False
		runLoop2 = True
		print("Running...")
	else:
		print("Invalid input. Please enter a correct input.")
		#print("2 - Tank mode - ")

def motorMove(dir1, dir2)
	#if dir1 != 0:
	if dir2 != 0: #Both motors
		print("Moving both motors")
		RPL.servoWrite(mtrLeft, dir1)
		RPL.servoWrite(mtrRight, dir2)
	else: #Left motor
		print("Moving left motor")
		RPL.servoWrite(mtrLeft, dir1)
		RPL.servoWrite(mtrRight, 1500)
	elif dir2 != 0: #Right motor
		print("Moving right motor")
		RPL.servoWrite(mtrLeft, 1500)
		RPL.servoWrite(mtrRight, dir2)
	else:
		print("Halting both motors")
			RPL.servoWrite(mtrLeft, 1500)
			RPL.servoWrite(mtrRight, 1500)
		clearText()

def interrupted(signum, frame): #copied from resource
	motorMove(0, 0)

signal.signal(signal.SIGALRM, interrupted) #copied from resource
tty.setraw(sys.stdin.fileno()) #copied from resource

SHORT_TIMEOUT = 0.255 #copied from resource
while runLoop2 == True:
	signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) #copied from resource
	input = sys.stdin.read(1) #copied from resource;
	signal.setitimer(signal.ITIMER_REAL, 0) #copied from resource;
	if input == "w":
		motorMove(2000, 1000)
	elif input == "a":
		motorMove(0, 1000)
	elif input == "s":
		motorMove(1000, 2000)
	elif input == "d":
		motorMove(2000, 0)
	elif input == "x":
		motorMove(0, 0)
	runMoop2 = False
