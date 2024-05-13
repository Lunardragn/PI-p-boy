import machine
import time

print("Boot finished")

# Define UART for GPIO serial communication
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))
led = machine.Pin(25, machine.Pin.OUT)  # Assuming LED pin is GPIO 25

# Dictionary to map mode strings to actual pin modes
mode_map = {
    'a': 'analog',
    'd': 'input',
    'p': 'output',
}

# Dictionary to map pin numbers to Pin objects
pin_map = {
    2: machine.Pin(2),
    3: machine.Pin(3),
    4: machine.Pin(4),
    5: machine.Pin(5),
    6: machine.Pin(6),
    7: machine.Pin(7),
    8: machine.Pin(8),
    9: machine.Pin(9),
    10: machine.Pin(10),
    11: machine.Pin(11),
    12: machine.Pin(12),
    13: machine.Pin(13),
}

# Initialize command buffer
command_buffer = ""

# Main loop to continuously listen for commands over GPIO serial
while True:
    if uart.any():
        led.on()
        received_char = uart.read(1).decode()

        # Echo the received character back to UART terminal
        uart.write(received_char)

        # Check if received character is Enter key
        if received_char == '\r':
            # Process command
            command = command_buffer.strip().split()
            if len(command) >= 3:
                action = command[0]
                pin_number = int(command[1])
                mode = command[2]

                if pin_number in pin_map:
                    pin = pin_map[pin_number]

                    if action.lower() == 'read':
                        if mode.lower() == 'a':
                            if pin_map[pin_number].__class__ == machine.ADC:
                                uart.write('\n' + str(pin.read_u16())+ '\n')
                            else:
                                uart.write("Pin {} is not configured as an analog input.\n".format(pin_number))
                        elif mode.lower() == 'd':
                            if pin_map[pin_number].__class__ != machine.ADC:
                                uart.write('\n' + str(pin.value())+ '\n')
                            else:
                                uart.write("Pin {} is not configured as a digital input.\n".format(pin_number))
                        elif mode.lower() == 'p':
                            uart.write("Not applicable for PWM mode.\n")
                        else:
                            uart.write("Invalid mode.\n")
                    elif action.lower() == 'write':
                        if len(command) >= 4:
                            value = int(command[3])
                            if mode.lower() == 'a':
                                uart.write("Analog mode does not support writing.\n")
                            elif mode.lower() == 'd':
                                pin_map[pin_number].init(machine.Pin.OUT)
                                pin_map[pin_number].value(value)
                                uart.write("Value written to pin {}.\n".format(pin_number))
                            elif mode.lower() == 'p':
                                pin_map[pin_number].init(machine.Pin.OUT)
                                pin_map[pin_number].value(value)
                                uart.write("Value written to pin {}.\n".format(pin_number))
                            else:
                                uart.write("Invalid mode.\n")
                        else:
                            uart.write("Insufficient parameters for write action.\n")
                elif action.lower() == 'read':
                    uart.write("Invalid pin number.\n")
                else:
                    uart.write("Invalid action.\n")
            else:
                uart.write("Invalid command format.\n")
            
            # Clear command buffer after processing
            command_buffer = ""
        elif received_char != '\n':  # Ignore newline characters
            # Add received character to command buffer
            command_buffer += received_char

        led.off()

