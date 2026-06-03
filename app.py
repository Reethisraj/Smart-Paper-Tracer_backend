from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from parser import extract_text
from matcher import compare_answers

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/analyze", methods=["POST"])
def analyze():

    if "answer_key" not in request.files:
        return jsonify({
            "error":"answer_key missing"
        }),400

    if "student_sheet" not in request.files:
        return jsonify({
            "error":"student_sheet missing"
        }),400

    answer_key_file = request.files["answer_key"]
    student_file = request.files["student_sheet"]

    answer_path = os.path.join(
        UPLOAD_FOLDER,
        answer_key_file.filename
    )

    student_path = os.path.join(
        UPLOAD_FOLDER,
        student_file.filename
    )

    answer_key_file.save(answer_path)
    student_file.save(student_path)

    answer_text = extract_text(answer_path)
    student_text = extract_text(student_path)

  

    result = compare_answers(
        answer_text,
        student_text
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

