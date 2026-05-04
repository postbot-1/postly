from flask import Flask, request, jsonify
import os
from app.core.executor import execute_post

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "Postly API Running 🚀"


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"filepath": filepath})


@app.route("/post", methods=["POST"])
def post():
    data = request.json

    results = execute_post(
        data["filepath"],
        data.get("caption", ""),
        data.get("title", ""),
        data.get("accounts", []),
        data.get("accounts_data", {})
    )

    return jsonify(results)


if __name__ == "__main__":
    app.run(port=5000)
