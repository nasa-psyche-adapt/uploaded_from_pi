#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as GPIO

###### First motor ######
DIR = 4   # Direction GPIO Pin
STEP = 12  # Step GPIO Pin
#########################

###### Second motor ######
DIR2 = 17   # Direction GPIO Pin
STEP2 = 27  # Step GPIO Pin
#########################

###### Third motor ######
DIR3 = 6   # Direction GPIO Pin
STEP3 = 5  # Step GPIO Pin
#########################

###### Fourth motor ######
DIR4 = 26   # Direction GPIO Pin
STEP4 = 16  # Step GPIO Pin
#########################

###### Fifth motor ######
DIR5 = 20   # Direction GPIO Pin
STEP5 = 21  # Step GPIO Pin
#########################

###### Sixth motor ######
DIR6 = 14   # Direction GPIO Pin
STEP6 = 15  # Step GPIO Pin
#########################

###### Seventh motor ######
DIR7 = 13   # Direction GPIO Pin
STEP7 = 19  # Step GPIO Pin
#########################

###### 8th motor ######
DIR8 = 11   # Direction GPIO Pin
STEP8 = 9  # Step GPIO Pin
#########################

###### 9th motor ######
DIR9 = 8   # Direction GPIO Pin
STEP9 = 25  # Step GPIO Pin
#########################

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)
kelly = 10

GPIO.setmode(GPIO.BCM)


###### First motor ######
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
#########################

###### second motor ######
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

#########################

###### Third motor ######
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)

#########################

###### Fourth motor ######
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)

#########################

###### Fifth motor ######
GPIO.setup(DIR5, GPIO.OUT)
GPIO.setup(STEP5, GPIO.OUT)

#########################

###### Sixth motor ######
GPIO.setup(DIR6, GPIO.OUT)
GPIO.setup(STEP6, GPIO.OUT)

#########################

###### Seventh motor ######
GPIO.setup(DIR7, GPIO.OUT)
GPIO.setup(STEP7, GPIO.OUT)

#########################

###### 8th motor ######
GPIO.setup(DIR8, GPIO.OUT)
GPIO.setup(STEP8, GPIO.OUT)

#########################

###### 9th motor ######
GPIO.setup(DIR9, GPIO.OUT)
GPIO.setup(STEP9, GPIO.OUT)

#########################

print("CW")
sleep(1)
step_count = SPR
delay = .0208

###### SLP/RST #######
GPIO.setup(kelly, GPIO.OUT)
GPIO.output(kelly, GPIO.HIGH)

###### First motor ######
GPIO.output(DIR, CW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    print(x)
    GPIO.output(STEP, GPIO.LOW)
    
    sleep(delay)

sleep(.5)
print("done")
sleep(1)
GPIO.output(DIR, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
#########################


###### second motor ######
GPIO.output(DIR2, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR2, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
#########################

###### Third motor ######
GPIO.output(DIR3, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR3, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
#########################

###### Fourth motor ######
GPIO.output(DIR4, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP4, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR4, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP4, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)
#########################

###### Fifth motor ######
GPIO.output(DIR5, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP5, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP5, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR5, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP5, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP5, GPIO.LOW)
    sleep(delay)
# ~ #########################

###### sixth motor ######
GPIO.output(DIR6, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP6, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP6, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR6, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP6, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP6, GPIO.LOW)
    sleep(delay)
#########################

###### Seventh motor ######
GPIO.output(DIR7, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP7, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP7, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR7, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP7, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP7, GPIO.LOW)
    sleep(delay)
#########################

###### 8th motor ######
GPIO.output(DIR8, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP8, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP8, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR8, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP8, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP8, GPIO.LOW)
    sleep(delay)
#########################

###### 9th motor ######
GPIO.output(DIR9, CW)
print("CW")
for x in range(step_count):
    GPIO.output(STEP9, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP9, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR9, CCW)
print("CCW")
sleep(1)
for x in range(step_count):
    GPIO.output(STEP9, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP9, GPIO.LOW)
    sleep(delay)
#########################

GPIO.setup(23, GPIO.OUT)
pwm=GPIO.PWM(23, 50)
pwm.start(0)

def SetAngle(angle):
	print("start of def")
	duty = angle / 18 + 2
	GPIO.output(23, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(23, False)
	pwm.ChangeDutyCycle(0)
	print("end of def")
	
SetAngle(90)
sleep(.1)
SetAngle(180) 
sleep(.1)
SetAngle(90) 
sleep(.1)
pwm.stop()


GPIO.output(kelly, GPIO.LOW)
GPIO.cleanup()
