from flask import Flask, request, jsonify
import time
 
app = Flask(__name__)
 
latest_data = {}
 
@app.route("/", methods=["GET"])
def home():
    return "ESP32 IMU Server Running"
 
@app.route("/imu", methods=["POST"])
def imu():
    global latest_data
 
    latest_data = request.json
 
    print(time.strftime("%H:%M:%S"), latest_data)
 
    return {"status": "ok"}, 200
 
@app.route("/latest", methods=["GET"])
def latest():
    return jsonify(latest_data)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
