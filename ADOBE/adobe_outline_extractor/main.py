# from flask import Flask, request, render_template, jsonify
# import os
# from extractor.heading_extractor import extract_headings

# UPLOAD_FOLDER = "uploaded_pdfs"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route("/")
# def index():
#     return render_template("upload.html")

# @app.route("/upload", methods=["POST"])
# def upload():
#     if "pdf_file" not in request.files:
#         return "No file uploaded", 400

#     file = request.files["pdf_file"]
#     if file.filename == "":
#         return "No selected file", 400

#     if file and file.filename.endswith(".pdf"):
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)

#         result = extract_headings(filepath)

#         return jsonify(result)

#     return "Invalid file type", 400

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, render_template, jsonify
import os
from extractor.heading_extractor import extract_headings

UPLOAD_FOLDER = "uploaded_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "pdf_file" not in request.files:
        return "No file uploaded", 400

    file = request.files["pdf_file"]
    if file.filename == "":
        return "No selected file", 400

    if file and file.filename.endswith(".pdf"):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        title, headings = extract_headings(filepath)

        return render_template("upload.html", title=title, headings=headings)

    return "Invalid file type", 400

if __name__ == "__main__":
    app.run(debug=True)
