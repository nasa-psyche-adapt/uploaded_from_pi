#!/usr/bin/env python3


from multiprocessing import Process
from time import sleep
import RPi.GPIO as GPIO87

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
GPIO.setmode(GPIO.BCM)


def func1():
	print('func1: starting')
	for i in range(10000000): pass
	print('func1: finishing')

def func2():
	print('func2: starting')
	for i in range(10000000): pass
	print('func2: finishing')


if __name__ == '__main__':
	p1 = Process(target=func1)
	p1.start()
	p2 = Process(target=func2)
	p2.start()
	p1.join()
	p2.join()


def runInParallel(*fns):
	proc = []
	for fn in fns:
		p = Process(target=fn)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()


runInParallel(func1, func2)


