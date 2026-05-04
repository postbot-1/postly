from flask import Flask, jsonify
from app.core.executor import execute_post

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "Postly API is running"})


@app.route("/run", methods=["GET"])
def run_post():
    try:
        result = execute_post()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    # IMPORTANT: Railway requires 0.0.0.0
    app.run(host="0.0.0.0", port=5000)
