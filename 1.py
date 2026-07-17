from flask import Flask, jsonify
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def home():
    """Returns a JSON payload with dynamic server uptime."""
    uptime = round(time.time() - START_TIME, 2)
    return jsonify({
        "status": "online",
        "uptime_seconds": uptime,
        "message": "System active."
    })

@app.route('/health')
def health_check():
    """Standard endpoint for load balancers or container orchestration."""
    return "OK", 200

if __name__ == '__main__':
    # debug=True automatically reloads the server on code changes
    app.run(host='0.0.0.0', port=5000, debug=True)