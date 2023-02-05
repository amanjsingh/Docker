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

# [6]		“os.path — Common Pathname Manipulations.”  _Python Documentation_, 
#         docs.python.org/3/library/os.path.html.



from flask import Flask, request
import json
import os
import requests

app = Flask(__name__)


@app.route("/checksum", methods=["POST"])
def validator():
    request_body = request.get_json()
    if request_body:
        if "file" in request_body and request_body.get("file"):
            file_name = request_body.get("file")
            path = "./data/" + file_name
            if os.path.isfile(path):
                hash = requests.post("http://calculator:3000/calculate", json=request_body)
                request_body["checksum"] = hash.text
            else:
                request_body["error"] = "File not found."
        else:
            request_body["error"] = "Invalid JSON input."
    else:
        request_body = {}
        request_body["error"] = "Invalid JSON input."

    return json.dumps(request_body)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
