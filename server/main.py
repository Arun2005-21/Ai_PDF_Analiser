from flask import Flask, jsonify, request
from PyPDF2 import PdfReader
import io
from flask_cors import CORS
from ollama import chat

app = Flask(__name__)

# Allow frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route("/api", methods=["POST"])
def api():
    try:
        if "pdf" not in request.files:
            return jsonify({"error": "No PDF file sent"}), 400

        pdf_file = request.files["pdf"]
        pdf_bytes = pdf_file.read()

        reader = PdfReader(io.BytesIO(pdf_bytes))

        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if text.strip() == "":
            return jsonify({"error": "No text found in PDF"}), 400

        response = chat(
    model="deepseek-r1:1.5b",
    messages=[
        {
            "role": "user",
            "content": f"""
You are an ATS Resume Reviewer and Career Coach.

Analyze the resume text below and return output in CLEAN MARKDOWN.

STRICT RULES:
- Use headings exactly as given
- Use bullet points only
- No long paragraphs
- Keep each bullet short (1 line)
- Do NOT invent experience
- If something is missing, mention it
- You MUST give an ATS score as a NUMBER from 0 to 100 (example: 67/100)
- Do NOT write "Missing" for ATS score

Return output ONLY in this structure:

## 📌 Candidate Overview
- Name:
- Target Role:
- Education:
- Experience Level:

## ⭐ ATS Score (0–100)
- ATS Score: XX/100
- Main Reason: (1 line)

## ✅ Strong Points
- 
- 
- 
- 
- 

## ❌ Weak Points / Missing Sections
- 
- 
- 
- 
- 

## 🔧 Improvements to Increase ATS Score
### 1) Formatting Improvements
- 
- 
- 

### 2) Content Improvements
- 
- 
- 

### 3) Keywords to Add (Role-Based)
- 
- 
- 

## 🎯 Best Suitable Job Roles
- 
- 
- 

## 🧠 Tips for Candidate
- 
- 
- 
- 
- 

Resume Text:
{text}
"""
        }
    ]
)



        return jsonify({"message": response.message.content})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
