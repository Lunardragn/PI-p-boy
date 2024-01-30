import gpiozero
import time

# Define GPIO pins for each module
SOUND_PIN = 17  # Example GPIO pin for sound sensor
DISTANCE_TRIGGER_PIN = 23  # Example GPIO pin for ultrasonic distance sensor (trigger)
DISTANCE_ECHO_PIN = 24  # Example GPIO pin for ultrasonic distance sensor (echo)
GPS_SERIAL_PORT = "/dev/ttyS0"  # Example serial port for GPS module

# Initialize GPIO devices
sound_sensor = gpiozero.DigitalInputDevice(SOUND_PIN)
distance_sensor = gpiozero.DistanceSensor(trigger=DISTANCE_TRIGGER_PIN, echo=DISTANCE_ECHO_PIN)
# You'll need to handle the GPS module's communication through serial port separately

def read_module(module):
    if module == "Sound":
        return sound_sensor.value  # Read sound sensor state
    elif module == "Ultrasonic Distance":
        return distance_sensor.distance * 100  # Read distance in centimeters
    elif module == "GPS":
        # Implement reading GPS data from serial port here
        return "GPS data"
    else:
        return "None"

def main():
    callout = "Current module: "
    module = "None"

    while True:
        current_module = int(input("Select module type (0=None, 1=Sound, 2=Ultrasonic Distance, 3=GPS): "))
        if current_module == 0:
            print(callout + "None")
            module = "None"
        elif current_module == 1:
            print(callout + "Sound")
            module = "Sound"
        elif current_module == 2:
            print(callout + "Ultrasonic Distance")
            module = "Ultrasonic Distance"
        elif current_module == 3:
            print(callout + "GPS")
            module = "GPS"
        else:
            print(callout + "None")
            module = "None"

        # Read from the selected module
        module_data = read_module(module)
        print("Data from {}: {}".format(module, module_data))
        time.sleep(1)  # Wait for 1 second before reading again

if __name__ == "__main__":
    main()
