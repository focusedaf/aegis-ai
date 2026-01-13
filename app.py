from flask import Flask,request,jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/")
def index():
    return "wsup"

# simulates img upload
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return {"error": "no file"}, 400

    file = request.files["file"]
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_DIR, filename)
    file.save(path)

    return jsonify({
        "status": "uploaded",
        "path": path
    })

# receive img
@app.route("/receive",methods=["POST"])
def receiveImg():
    data = request.json
    path = data.get("file_path")

    if not path:
        return {"error": "no file_path"}, 400

    return {"status": "received", "path": path}

# simulate video upload
@app.route("/uploadVid", methods=["POST"])    
def uploadVid():
    if "video" not in request.files:
        return {"error": "no video"}, 400

    video = request.files["video"]
    filename = secure_filename(video.filename)
    path = os.path.join(UPLOAD_DIR, filename)
    video.save(path)

    return jsonify({
        "status": "uploaded",
        "path": path
    })

# receive video
@app.route("/receiveVid",methods=["POST"])
def receiveVid():
    data = request.json
    path = data.get("video_path")

    if not path:
        return {"error": "no video_path"}, 400

    return {"status": "received", "path": path}

if __name__ in "__main__":
    app.run(debug=True)