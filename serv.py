from flask import Flask, request
import time
 
app = Flask(__name__)
 
@app.route("/imu", methods=["POST"])
def imu():
    data = request.json
 
    print(
        time.strftime("%H:%M:%S"),
        data,
        flush=True
    )
 
    return "OK", 200
 
 
@app.route("/", methods=["GET"])
def home():
    return "ESP32 IMU Server Running", 200
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
