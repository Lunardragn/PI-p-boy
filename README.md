# PI-pboy Mini
### The mega swiss army knife of wearable hardware. 
Designed for those who just really want an open source pipboy style wearable that's compatible with almost everything I guess

# NOTE:
This is currently untested, as I am still working on obtaining parts. 

Updates will be made after I get the components

### Are there better solutions?
Yeah, but I want to make this one mine, with all the bits and bobs I could ever want. Just uploading the stuff so anyone could make one if they wanted

# Hardware:
### Pi Zero 2w x1
### Waveshare V4 2.13 inch E-ink display hat x1
### Rotary Encoder x1
### Wrist strap of choice x1
### Pi Pico (for expansion shim, since the display hat will take up GPIO space)
### Pisugar 3

# Dependencies:
### pyautogui
### RPi.GPIO
### python-opencv python3-opencv opencv-data
### mediapipe-rpi3
### mediapipe-rpi4
### gtts
### mpyg321
### spidev

# TO DO:

### GPIO based Serial console, because why not
### Implement a custom GUI, to select from a list of apps.
### GPS compatibility via UBLOX-7 module.
### "Graceful" Desktop interaction 
(Onscreen keyboard, etc).
### KDE Connect stuff, make it like a smart watch.
### Modular GPIO, allowing for custom modules to be slapped into it and interacted with 
(I.E: Thermometer, laser distance sensor, MQ series gas sensors).
### A way for the PI to figure out what its connected to. 
(Could be temporarily solved with a dropdown menu to select what's installed, though that seems cumbersome)
### Proper setup guide.
### Custom assets 
(Boot screen, buttons, fonts).
### Modded 3d printed case, to allow for a bigger battery, interfacing for custom modules
(I'm not sure how far the twin rotary encoders can go in terms of being "comfortable").
### Camera, object detection, and pose tracking toggle for fun
### Zero Light Mapping via 360 LIDAR module
### Support for servo and stepper motor testing maybe?
### Controller expansion
### Pentesting stuff?
### The ability to switch between the custom GUI and a destop environment. 
It's a mini PC, why the heck not?
### Set up quicksetup.sh

# Modules:
### Microphone - Ambient or direct sound measuring
Raise a warning if it goes past a certain threshold, as a means of protecting hearing
### Laser Distance
### Ultrasonic distance
### MQ series sensors - Gas 
### CO2 sensor - MH-Z16 for this version
### Dust sensor - Waveshare Sharp GP2Y1010AU0F 
### Environment sensor
### 360 LIDAR
### Controller expansion
Make it so custom controls like joysticks or extra rotary encoders can be plugged in to control things connected through GPIO. Like, two servos controlled with a couple rotary encoders, or a joystick. 
I want to support at least 3 additional inputs. Really stretching the GPIO pins of the pi thin... might need a co-processor like a Pico to recieve serial and expand the overall GPIO. need to make a circut diagram first.
### Remote transmitter
Remote controlled arduino stuff maybe?

# Check out:

### https://github.com/SirLefti/piboy
### https://github.com/Zaryob/raspipboy
### https://core-electronics.com.au/guides/object-identify-raspberry-pi/
### https://core-electronics.com.au/guides/pose-and-face-landmark-raspberry-pi/
### https://learn.adafruit.com/raspberry-pi-pipboy-3000/
### These could be used as inspiration, modified they could do exactly what I need. I suppose this is my way of crediting these projects
