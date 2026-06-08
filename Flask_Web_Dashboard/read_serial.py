import serial

ser = serial.Serial('COM9', 115200)

while True:
    line = ser.readline().decode().strip()
    print(line)