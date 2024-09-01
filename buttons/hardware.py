import busio
import digitalio
import board
from adafruit_mcp230xx.mcp23017 import MCP23017
import time

class ResetException(Exception):
    pass

button_pins = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, 
               board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, 
               board.GP12, board.GP13, board.GP14, board.GP15, board.GP16]

buttons = []
for p in range(15):
    bt = digitalio.DigitalInOut(button_pins[p])
    bt.pull = digitalio.Pull.UP
    buttons.append(bt)

i2c = busio.I2C(sda=board.GP0, scl=board.GP1)
mcp = MCP23017(i2c)

led_pins = [mcp.get_pin(0), mcp.get_pin(1), mcp.get_pin(2), mcp.get_pin(3), mcp.get_pin(4), 
            mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7), mcp.get_pin(8), mcp.get_pin(9), 
            mcp.get_pin(10), mcp.get_pin(11), mcp.get_pin(12), mcp.get_pin(13), mcp.get_pin(14)]

leds = []
for p in range(15):
    led = mcp.get_pin(p)
    led.switch_to_output(value=True)
    led.value = False
    leds.append(led)

def set_leds(data):
    for i in range(15):
        leds[i].value = data[i]

def get_buttons():
    data = []
    for i in range(15):
        data.append(not buttons[i].value)
    return data

def wait_buttons_released():
    while True:
        data = get_buttons()
        if True not in data:
            break

def wait_button_press(blink=[]):
    blink_reload = 2
    blink_time = blink_reload
    blink_value = False    
    while True:   
        blink_time -= 1
        if blink_time<0:  
            blink_time = blink_reload   
            for i in blink:
                leds[i].value = blink_value
            blink_value = not blink_value
        data = get_buttons()
        a = data[0]
        b = data[10]
        c = data[14]
        if a and b or a and c or b and c:
            # Two of the three corners are pressed ... bail out
            raise ResetException()
        if True not in data:
            break
        time.sleep(0.1)
    blink_time = blink_reload
    while True:        
        blink_time -= 1
        if blink_time<0:  
            blink_time = blink_reload   
            for i in blink:
                leds[i].value = blink_value
            blink_value = not blink_value
        data = get_buttons()
        if True in data:
            return data.index(True)
        time.sleep(0.1)
    

