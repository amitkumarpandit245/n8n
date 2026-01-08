
# PDF Classification & Information Extraction Platform

## Setup (Windows)
1. Install Python 3.10+
2. Install n8n (npm install -g n8n)
3. Install requirements: pip install flask requests reportlab

## Environment Variables
- GEMINI_API_KEY
- N8N_WEBHOOK_URL

## n8n Workflow Import
1. Open n8n UI
2. Import workflow JSON (provided separately)
3. Configure webhook URL

## Run
python ui/app.py
