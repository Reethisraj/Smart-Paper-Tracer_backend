Smart Paper Tracer - Backend

overview:
This is the backend service for the Smart Paper Tracer project built using Flask. It handles OCR-based processing of uploaded answer sheets, extracts text from files, compares student answers with the answer key, and returns evaluation results through a REST API.

Features:
Upload answer key and student answer sheets
OCR-based text extraction using Tesseract
Answer comparison and scoring system
Returns structured JSON response
REST API for frontend integration

Tech Stack:
Python
Flask
Flask-CORS
Tesseract OCR (pytesseract)
OpenCV
NumPy
API Endpoint
POST /analyze

Description: Compares answer key with student sheet and returns evaluation results.

Form Data:
answer_key (file)
student_sheet (file)

Response Example:
{
"student_name": "John",
"roll_no": "12",
"total_score": 85,
"results": [
{
"question": "Q1",
"answer": "Water evaporates",
"student": "Water changes due to heat",
"score": 80
}
]
}

Deployment:
Backend deployed using Render.

Start Command:
python app.py

Build Command:
pip install -r requirements.txt

Note:
This is a prototype project and OCR accuracy depends on input quality.

Author

RRJ
