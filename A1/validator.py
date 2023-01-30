from flask import Flask, request
import json
import os

app = Flask(__name__)


@app.route("/checksum", methods=["POST"])
def validator():
    request_body = request.get_json()
    print("\nDictionary :", request_body)
    if request_body:
        if "file" in request_body and request_body.get("file"):
            file_name = request_body.get("file")
        else:
            request_body["error"] = "Invalid JSON input."
            print("\nJSON :", request_body)
            return json.dumps(request_body)
    else:
        request_body = {}
        request_body["error"] = "Invalid JSON input."
        return json.dumps(request_body)

    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
