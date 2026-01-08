from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os, uuid, requests
import os

load_dotenv()  # loads .env into environment



app = Flask(__name__)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    doc_id = str(uuid.uuid4())
    path = os.path.join(UPLOAD_DIR, doc_id + ".pdf")
    f.save(path)
    requests.post(N8N_WEBHOOK_URL, json={"document_id": doc_id, "file_path": path})
    return jsonify({"document_id": doc_id, "status": "queued"})

if __name__ == "__main__":
    app.run(debug=True)
