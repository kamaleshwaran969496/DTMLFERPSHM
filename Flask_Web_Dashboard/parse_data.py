import serial

ser = serial.Serial('COM9', 115200)

while True:

    line = ser.readline().decode().strip()

    data = line.split(',')

    if len(data) == 9:

        bpm = float(data[0])
        spo2 = float(data[1])
        temp = float(data[2])
        hum = float(data[3])

        ax = float(data[4])
        ay = float(data[5])
        az = float(data[6])

        lat = float(data[7])
        lon = float(data[8])

        print("\n===== SOLDIER DATA =====")
        print("BPM       :", bpm)
        print("SpO2      :", spo2)
        print("Temp      :", temp)
        print("Humidity  :", hum)
        print("AX        :", ax)
        print("AY        :", ay)
        print("AZ        :", az)
        print("Latitude  :", lat)
        print("Longitude :", lon)