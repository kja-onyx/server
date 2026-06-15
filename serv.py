from flask import Flask, request, jsonify
import time
 
app = Flask(__name__)
 
all_data = []
 
@app.route("/", methods=["GET"])
def home():
    return "ESP32 IMU Server Running"
 
@app.route("/imu", methods=["POST"])
def imu():
 
    data = request.json
 
    all_data.append(data)
 
    # Keep last 5000 samples
    if len(all_data) > 5000:
        all_data.pop(0)
 
    print(time.strftime("%H:%M:%S"), data)
 
    return {"status": "ok"}, 200
 
@app.route("/latest", methods=["GET"])
def latest():
 
    if len(all_data) == 0:
        return jsonify({})
 
    return jsonify(all_data[-1])
 
@app.route("/all", methods=["GET"])
def all_samples():
 
    return jsonify(all_data)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
