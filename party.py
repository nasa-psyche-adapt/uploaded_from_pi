from time import sleep
import board
import busio
import digitalio
 
from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)  # MCP23017

# step
pin0 = mcp.get_pin(0)

# slp/rst
pin1 = mcp.get_pin(1)

# dir
pin8 = mcp.get_pin(8)


pin0.switch_to_output(value=True)
pin1.switch_to_output(value=True)
pin8.switch_to_output(value=True)

# slp/rst
pin1.value = True

CW = 1      # Clockwise Rotation
CCW = 0     # Counterclockwise Rotation
SPR = 48    # Steps per Revolution (360 / 7.5)
kelly = 10

print("CW")
sleep(1)
step_count = SPR
delay = .0208

pin8.value = True
# GPIO.output(DIR, CW)
for x in range(step_count):

    pin0.value = True
    # GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    print(x)
    pin0.value = False
    # GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
print("done")
sleep(1)
pin8.value = True
# GPIO.output(DIR, CCW)
print("CCW")
sleep(1)
for x in range(step_count):

    pin0.value = True
    # GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    print(x)
    pin0.value = False
    # GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    
pin1.value = False
