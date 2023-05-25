import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)  # Update the port if necessary

with open('signal.txt', 'w') as file:
    while True:
        line = ser.readline().decode().strip()

        if line:
            # Store the received signals in the file
            file.write(line + '\n')
            file.flush()