import os
import uuid
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file or not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files allowed"}), 400

    document_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{document_id}.pdf")
    file.save(file_path)

    requests.post(
        N8N_WEBHOOK_URL,
        json={
            "document_id": document_id,
            "file_path": os.path.abspath(file_path)
        }
    )

    return jsonify({
        "document_id": document_id,
        "status": "queued"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
