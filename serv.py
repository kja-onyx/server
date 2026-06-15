from flask import Flask, request, send_file

import csv

import os

from datetime import datetime
app = Flask(name)
CSV_FILE = "imu_data.csv"
Create CSV file with header if it doesn't exist
if not os.path.exists(CSV_FILE):

with open(CSV_FILE, "w", newline="") as f:

writer = csv.writer(f)

writer.writerow([

"timestamp",

"esp_ms",

"ax",

"ay",

"az",

"gx",

"gy",

"gz"

])
@app.route("/")

def home():

return "ESP32 IMU Server Running"
@app.route("/imu", methods=["POST"])

def imu():
data = request.json
timestamp = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S.%f"
)[:-3]
with open(CSV_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        timestamp,
        data.get("esp_ms"),
        data.get("ax"),
        data.get("ay"),
        data.get("az"),
        data.get("gx"),
        data.get("gy"),
        data.get("gz")
    ])
return {"status": "ok"}, 200
@app.route("/csv")

def download_csv():
return send_file(
    CSV_FILE,
    as_attachment=True,
    download_name="imu_data.csv"
)
if name == "main":

app.run(host="0.0.0.0", port=10000)
 
