#!/usr/bin/env python3


from time import sleep
import board
import busio
import digitalio
import RPi.GPIO as GPIO

from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)  # MCP23017
kelly = 7

GPIO.setmode(GPIO.BCM)

# ~ ###### First motor ######
# ~ DIR =  11  # Direction GPIO Pin
# ~ STEP =  8 # Step GPIO Pin
# ~ #########################

# ~ ###### SLP/RST #######
# ~ GPIO.setup(kelly, GPIO.OUT)
# ~ GPIO.output(kelly, GPIO.HIGH)

# ~ ###### First motor ######
# ~ GPIO.setup(DIR, GPIO.OUT)
# ~ GPIO.setup(STEP, GPIO.OUT)
# ~ #########################

# ~ # dir
pin8 = mcp.get_pin(9)

# step
pin0 = mcp.get_pin(10)

# slp/rst
pin1 = mcp.get_pin(11)

pin0.switch_to_output(value=True)
pin1.switch_to_output(value=True)
pin8.switch_to_output(value=True)

# slp/rst
pin1.value = True

CW = 1      # Clockwise Rotation
CCW = 0     # Counterclockwise Rotation
SPR = 48    # Steps per Revolution (360 / 7.5)

print("CW")
sleep(1)
step_count = SPR
delay = .0208

pin8.value = True
# ~ GPIO.output(DIR, CW)
for x in range(step_count):

    pin0.value = True
    # ~ GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    print(x)
    pin0.value = False
    # ~ GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
print("done")
sleep(1)
pin8.value = False
# ~ GPIO.output(DIR, CCW)
print("CCW")
sleep(1)
for x in range(step_count):

    pin0.value = True
    # ~ GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    print(x)
    pin0.value = False
    # ~ GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    
pin1.value = False
GPIO.cleanup()
