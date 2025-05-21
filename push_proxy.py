
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

RENDER_URL = "https://lisy-pusher.onrender.com/external"
AUTH_TOKEN = "secret-from-your-env"

@app.route("/relay", methods=["POST"])
def relay():
    data = request.get_json()
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    try:
        response = requests.post(RENDER_URL, json=data, headers=headers)
        return jsonify({"relay_status": response.status_code}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
