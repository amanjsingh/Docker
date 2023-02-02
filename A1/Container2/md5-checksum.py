from flask import Flask, request
import os
import hashlib

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate_checksum():
    request_body = request.get_json()
    if request_body and "file" in request_body:
        file_name = "./data/" + request_body.get("file")
        with open(file_name, "r") as file:
            content_bytes = file.read().encode()
            hash = hashlib.md5(content_bytes).hexdigest()
            return hash


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
