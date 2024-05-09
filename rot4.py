import RPi.GPIO as GPIO
import time
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
# Define GPIO pins
sw_pin = 23
dt_pin = 24
clk_pin = 25

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO pins
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables to track encoder state and set up E-Paper
encoder_prev_clk_state = GPIO.input(clk_pin)
counter = 0
sw_prev_state = GPIO.input(sw_pin)
epd = epd2in13_V4.EPD()
logging.info("init and Clear")
epd.init()
epd.Clear(0xFF)
font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame 
draw = ImageDraw.Draw(image)
try:
    print("Rotary encoder testing started. Turn the encoder to see the counter change.")
    while True:
        dt_state = GPIO.input(dt_pin)
        clk_state = GPIO.input(clk_pin)
        sw_state = GPIO.input(sw_pin)
        
        if clk_state != encoder_prev_clk_state:
            if dt_state != clk_state:
                counter += 1
                print("Counter incremented:", counter)
                draw.text((120, 60), 'Counter: ', counter, font = font15, fill = 0)
            else:
                counter -= 1
                print("Counter decremented:", counter)
                draw.text((120, 60), 'Counter: ', counter, font = font15, fill = 0)
                
            encoder_prev_clk_state = clk_state

        if sw_state == GPIO.LOW and sw_prev_state == GPIO.HIGH:
            counter = 0
            print("Counter reset")
        
        sw_prev_state = sw_state
        logging.info("E-paper refreshes quickly")
        epd.init_fast()
        time.sleep(0.01)  # Adjust sleep time as needed

except KeyboardInterrupt:
    print("\nExiting program.")
    GPIO.cleanup()
