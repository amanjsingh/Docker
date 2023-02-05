### References
# [1]		“Python for Beginners – Full Course [Programming Tutorial].” YouTube, 
#         www.youtube.com/watch?v=eWRfhZUzrAc.

# [2]		Srivastav, Prakhar. “A Docker Tutorial for Beginners.” A Docker Tutorial for Beginners,
#         docker-curriculum.com.

# [3]		“Python Requests Post Method.”  _Python Requests Post Method_, 
#         www.w3schools.com/python/ref_requests_post.asp.

# [4]		“Quickstart — Requests 2.28.2 Documentation.”  _Quickstart — Requests 2.28.2 Documentation_, 
#         requests.readthedocs.io/en/latest/user/quickstart.

# [5]		“7. Input and Output.”  _Python Documentation_, 
#         docs.python.org/3/tutorial/inputoutput.html.

# [6]		“MD5 Message Digest Algorithm &Mdash.”  _MD5 Message Digest Algorithm &Mdash_, 
#         python.readthedocs.io/en/v2.7.2/library/md5.html.

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
