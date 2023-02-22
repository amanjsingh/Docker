from flask import Flask, request
import boto3
import json
import requests

app = Flask(__name__)


@app.route("/storedata", methods=["POST"])
def write_data():
    request_body = request.get_json()
    data = request_body.get("data")

    file = open("data.txt", "w")
    file.write(data)
    file.close()

    session = get_session()
    s3 = session.resource("s3")
    s3.Bucket("amanjot-bucket").put_object(Key="data.txt", Body=data)
    return json.dumps(request_body)


@app.route("/appenddata", methods=["POST"])
def append_data():
    request_body = request.get_json()
    new_data = request_body.get("data")
    old_data = read_data()
    data = old_data + new_data

    file = open("data.txt", "w")
    file.write(data)
    file.close()

    session = get_session()
    s3 = session.resource("s3")
    s3.Bucket("amanjot-bucket").put_object(Key="data.txt", Body=data)
    return json.dumps(request_body)


@app.route("/deletefile", methods=["POST"])
def delete_file():
    request_body = request.get_json()
    file_url = request_body.get("s3uri")

    url_tokens = file_url.split("/")
    bucket_name = url_tokens[2]
    file_name = url_tokens[len(url_tokens) - 1]

    session = get_session()
    s3 = session.resource("s3")
    obj = s3.Object("amanjot-bucket", "data.txt")
    return obj.delete()


@app.route("/readdata")
def read_data():
    try:
        session = get_session()
        s3 = session.resource("s3")
        obj = s3.Object("amanjot-bucket", "data.txt")
        body = obj.get()["Body"].read()
        return body.decode()
    except Exception as e:
        print("Exception")
        print(str(e))
        return 400


def get_session():
    try:
        session = boto3.Session(
            aws_access_key_id="ASIA6NRSAKFKBT2MMAGJ",
            aws_secret_access_key="fbAk5Ai4ao1ABMi0qEGyPmuG11PplcWFq54eOFkv",
            aws_session_token="FwoGZXIvYXdzEEIaDAo49TiNSKbZi59hRyLAAaQwdqva+L2ylIiUCaYWIT+3R9Wys+/XwYYTWP6737Ln9u/lF7FTAnf0OfSF62MVX4oy13daiOFNE4u/KcGXecXwldTUGBxzdjYx5Yns0SUbRx9xl8Z3Z+qZooOVFumnRwpdqEOSN0ViIFHGbl/ur5fETk7nsPIk6QgxBp6gKahfoJLoK5nQMzPtTL3YuFtXR7OOt6cPNKz0ZWJlT47+cTnpJzoE5FCkHgqbypEUkrD7dwP/nR0gIPayfalTDn7bhij+v9WfBjItJXTUQuTwgf4DnE+WV2XHmV/H2s8ABaPR/hhsPaAHOuh7ljeXkTuB7g4vTZX6",
            region_name="us-east-1",
        )
        return session
    except Exception as e:
        print("Exception")
        print(str(e))
        return 400
