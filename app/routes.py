from flask import Blueprint, render_template, request, send_file
from app.utils import process_word_file
import os

# 定義 Blueprint
main = Blueprint("main", __name__)

# 資料夾路徑
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

# 確保目錄存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename.endswith(".docx"):
            input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            output_path = os.path.join(PROCESSED_FOLDER, f"processed_{uploaded_file.filename}")
            uploaded_file.save(input_path)

            # 處理文件
            process_word_file(input_path, output_path)

            return render_template("result.html", file_url=f"/download/{os.path.basename(output_path)}")
        else:
            return "<p>請上傳 .docx 文件！</p>"
    return render_template("index.html")

@main.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join(PROCESSED_FOLDER, filename), as_attachment=True)
