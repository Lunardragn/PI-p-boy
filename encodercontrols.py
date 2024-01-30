import RPi.GPIO as GPIO
import time
import pyautogui

# GPIO Pins for the encoders
X_CLK_PIN = 17
X_DT_PIN = 18
Y_CLK_PIN = 27
Y_DT_PIN = 22
X_BTN_PIN = 23
Y_BTN_PIN = 24

# Initialize PyAutoGUI for mouse control
pyautogui.FAILSAFE = False

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(X_CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(X_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Y_CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Y_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(X_BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Y_BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize variables for encoder state
x_clk_last_state = GPIO.input(X_CLK_PIN)
x_counter = 0
y_clk_last_state = GPIO.input(Y_CLK_PIN)
y_counter = 0

# Function to handle X encoder rotation
def x_encoder_callback(channel):
    global x_clk_last_state, x_counter
    clk_state = GPIO.input(X_CLK_PIN)
    dt_state = GPIO.input(X_DT_PIN)
    if clk_state != x_clk_last_state:
        if dt_state != clk_state:
            x_counter += 1
        else:
            x_counter -= 1
    x_clk_last_state = clk_state

# Function to handle Y encoder rotation
def y_encoder_callback(channel):
    global y_clk_last_state, y_counter
    clk_state = GPIO.input(Y_CLK_PIN)
    dt_state = GPIO.input(Y_DT_PIN)
    if clk_state != y_clk_last_state:
        if dt_state != clk_state:
            y_counter += 1
        else:
            y_counter -= 1
    y_clk_last_state = clk_state

# Function to handle mouse button press
def mouse_button_callback(channel):
    if channel == X_BTN_PIN:
        pyautogui.click(button='left')
    elif channel == Y_BTN_PIN:
        pyautogui.click(button='right')

# Setup interrupt callbacks for encoder rotation
GPIO.add_event_detect(X_CLK_PIN, GPIO.BOTH, callback=x_encoder_callback, bouncetime=5)
GPIO.add_event_detect(Y_CLK_PIN, GPIO.BOTH, callback=y_encoder_callback, bouncetime=5)

# Setup interrupt callback for mouse button press
GPIO.add_event_detect(X_BTN_PIN, GPIO.FALLING, callback=mouse_button_callback, bouncetime=300)
GPIO.add_event_detect(Y_BTN_PIN, GPIO.FALLING, callback=mouse_button_callback, bouncetime=300)

try:
    while True:
        # Update mouse position based on encoder counts
        pyautogui.moveRel(x_counter, y_counter, duration=0.1)
        x_counter = 0
        y_counter = 0
        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
