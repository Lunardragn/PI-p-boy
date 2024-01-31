# PI-pboy
### The mega swiss army knife of wearable hardware. 
Designed for those who just really want an open source pipboy style wearable that's compatible with almost everything I guess

# NOTE:
This is currently untested, as I am still working on obtaining parts. 

Updates will be made after I get the components

### Are there better solutions?
Yeah, but I want to make this one mine, with all the bits and bobs I could ever want. Just uploading the stuff so anyone could make one if they wanted

# Hardware:
### Pi 3 or 4 x1
### Rotary encoders x2
### GPS module x1 
(Pending implementation)
### Modded 3d printed case 
(In progress, needs foam for padding, and magnets to hold it closed. might make mounts for straps, in case it's too big)
### 3.5 inch LCD x1 
(This version is using an HDMI screen I snagged on Amazon)
### Pi camera/webcam 
x1
### Female to female jumper wires 
x??
### Real-Time Clock module 
x1 (pending implementation)
### Geiger counter module 
x1 (Couldn't resist, pending implementation)
### Adafruit Amp 
x1 (Adafruit Mono 2.5W Class D Audio Amplifier - PAM8302 [ADA2130])
### Adafruit PowerBoost 1000 and battery 
x1 (I chose a dual cell 5200mAh 3.7v Lithium ion Battery)
### Small plastic speaker 
x1 (Dimensions pending)
### LED and resistor of your choice 
x1 
### Slide switch for a power switch 
x1
### Pi Pico
x1 (Might change. Wanted to use it to handle inputs so the main pi has more free GPIO pins)

# Dependencies:
### pyautogui
### RPi.GPIO or gpiozero 
(Testing, need to find out which works better)
### opencv
### python-opencv python3-opencv opencv-data
### mediapipe-rpi3
### mediapipe-rpi4
### gtts
### mpyg321

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
