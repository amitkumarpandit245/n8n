
# PDF Classification & Information Extraction Platform

## Setup (Windows)
1. Install Python 3.10+
2. Install n8n (npm install -g n8n)
3. pip install -r requirements.txt

## Environment Variables
- GEMINI_API_KEY
- N8N_WEBHOOK_URL

## n8n Workflow Import
1. Open n8n UI
2. Import workflow JSON (provided separately)
3. Configure webhook URL

## Run
python .\ui\app.py
    -Upload Pdf by opening http://127.0.0.1:5000/
    -Files will get uploaded to uploads folder inside the project repo
python .\processor\processor_service.py
n8n start
open http://localhost:5678/ and execute your workflow in test mode
Use postman to create post request ny sending below payload
    URL:- http://localhost:5678/webhook-test/process-pdf
    Method: POST
    Request Body: 
    {
  "file_path":"\\pdf_platform_deliverables\\uploads\\52e53e07-c942-4f3e-a0af-6194f770816f.pdf",
  "document_id":"52e53e07-c942-4f3e-a0af-6194f770816f"
    }
This will start the n8n workflow
