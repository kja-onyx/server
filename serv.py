from flask import Flask, request, send_file, jsonify
import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

CSV_FILE = "imu_data.csv"

# Create CSV file with header if it doesn't exist
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
    try:
        data = request.get_json()

        timestamp = datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

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

        return jsonify({
            "status": "success",
            "timestamp": timestamp
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/csv")
def download_csv():
    return send_file(
        CSV_FILE,
        as_attachment=True,
        download_name="imu_data.csv"
    )


@app.route("/count")
def count_rows():
    with open(CSV_FILE, "r") as f:
        rows = sum(1 for _ in f) - 1

    return jsonify({
        "records": rows
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
