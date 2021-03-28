#!/usr/bin/env python3


from time import sleep
import board
import busio
import digitalio
import RPi.GPIO as GPIO

from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)  # MCP23017

GPIO.setmode(GPIO.BCM)



