import RPi.GPIO as GPIO
import time

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

# Variables to track encoder state
encoder_prev_clk_state = GPIO.input(clk_pin)
counter = 0
sw_prev_state = GPIO.input(sw_pin)

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
            else:
                counter -= 1
                print("Counter decremented:", counter)
                
            encoder_prev_clk_state = clk_state

        if sw_state == GPIO.LOW and sw_prev_state == GPIO.HIGH:
            counter = 0
            print("Counter reset")
        
        sw_prev_state = sw_state

        time.sleep(0.01)  # Adjust sleep time as needed

except KeyboardInterrupt:
    print("\nExiting program.")
    GPIO.cleanup()
