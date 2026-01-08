import os
import json
from google import genai

# Read API key from environment variable
GEMINI_API_KEY = "AIzaSyDhCwOrgLPLuYdcM7a6uC_Q_7dptSmPmxY"

client = genai.Client(api_key="AIzaSyDhCwOrgLPLuYdcM7a6uC_Q_7dptSmPmxY")


def classify_and_extract(text):
    prompt = f"""
You are an AI document classification and information extraction system.

Rules:
- Output ONLY valid JSON
- No markdown
- No explanations
- No extra text before or after JSON

Document text:
{text}

Classify into one of:
Invoice, Resume, Contract, Legal Document, Other

Extract fields:
Invoice -> invoice_number, vendor_name, invoice_date, total_amount
Resume -> name, skills, years_of_experience
Contract -> parties, start_date, end_date

Output:
{{
  "document_type": "",
  "extracted_data": {{}}
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return None

    try:
        # Gemini returns plain text
        raw_text = response.text.strip()

        # Defensive cleanup (in case Gemini adds whitespace)
        json_start = raw_text.find("{")
        json_end = raw_text.rfind("}") + 1

        if json_start == -1 or json_end == -1:
            print("No JSON object found in response.")
            return None

        clean_json = raw_text[json_start:json_end]
        return json.loads(clean_json)

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print("Raw response:", response.text)
        return None
