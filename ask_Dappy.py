import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
pwm=GPIO.PWM(23, 50)
pwm.start(0)
kelly = 10
###### Sixth motor ######
DIR6 = 8   # Direction GPIO Pin
STEP6 = 25  # Step GPIO Pin
#########################
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

###### Sixth motor ######
GPIO.setup(DIR6, GPIO.OUT)
GPIO.setup(STEP6, GPIO.OUT)
GPIO.setup(kelly, GPIO.OUT)
GPIO.output(kelly, GPIO.HIGH)
#########################

step_count = SPR
delay = .0208

def SetAngle(angle):
	print("start of def")
	duty = angle / 18 + 2
	GPIO.output(23, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(23, False)
	pwm.ChangeDutyCycle(0)
	print("end of def")
	
SetAngle(75)
while True:

	answer1 = input("Enter Dappy's answer: ")
	

	if answer1 == "yes":
		SetAngle(180)
	 
		sleep(.1)

		SetAngle(90)
	 
		sleep(.1)
	
	if answer1 == "no":
		###### sixth motor ######
		GPIO.output(DIR6, CW)
		
		for x in range(step_count):
			GPIO.output(STEP6, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP6, GPIO.LOW)
			sleep(delay)

		sleep(.5)
		GPIO.output(DIR6, CCW)
		sleep(1)
		for x in range(step_count):
			GPIO.output(STEP6, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP6, GPIO.LOW)
			sleep(delay)
			
#########################
GPIO.output(kelly, GPIO.LOW)
pwm.stop()
GPIO.cleanup()

