from flask import Flask, request, jsonify
import pdfplumber
import os
from gemini_client import classify_and_extract

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    file_path = request.get_json()['file_path']
    if not file_path or not os.path.exists(file_path):
        return {"error": "Invalid or missing file path"}, 400

    pages = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")

    full_text = "\n".join(pages)

    result = classify_and_extract(full_text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5002, debug=True)
