from flask import Flask, render_template, jsonify
import serial
import pickle
import pandas as pd
import threading
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

app = Flask(__name__)

# Load ML model
model = pickle.load(open("soldier_model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Serial connection
ser = serial.Serial('COM9', 115200)

# Global storage for latest data
latest_data = {
    "bpm": 0,
    "spo2": 0,
    "temp": 0,
    "hum": 0,
    "ax": 0,
    "ay": 0,
    "az": 0,
    "lat": 0,
    "lon": 0,
    "status": "Loading..."
}

# Background thread function
def read_serial():
    global latest_data

    while True:
        try:
            line = ser.readline().decode(errors='ignore').strip()
            print("RAW DATA:", line)

            if line.startswith("BPM"):
                continue

            data = line.split(',')

            if len(data) != 9:
                continue

            bpm, spo2, temp, hum, ax, ay, az, lat, lon = map(float, data)

            if (bpm == 0 or spo2 == 0 or temp == 0 or hum == 0 or
                ax == 0 or ay == 0 or az == 0 or lat == 0 or lon == 0):

                status = "Data_Inconsistency"

            else:
                sample = pd.DataFrame([[bpm, spo2, temp, hum, ax, ay, az]],
                                      columns=['BPM','SpO2','Temp','Humidity',
                                               'Motion(AX)','Motion(AY)','Motion(AZ)'])

                prediction = model.predict(sample)
                status = le.inverse_transform(prediction)[0]

            latest_data = {
                "bpm": bpm,
                "spo2": spo2,
                "temp": temp,
                "hum": hum,
                "ax": ax,
                "ay": ay,
                "az": az,
                "lat": lat,
                "lon": lon,
                "status": status
            }


        except Exception as e:
            print("Serial Error:", e)
            continue


# Routes
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data')
def data():
    return jsonify(latest_data)


# Start thread before Flask runs
threading.Thread(target=read_serial, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)