from flask import Flask, request
import json
import logging
import os

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app_port = os.getenv("APP_PORT", 8010)


@app.route("/documents", methods=["POST"])
def getDocuments():
    data = request.json
    print("Dokument otrzymany : " + json.dumps(data), flush=True)
    logging.debug("Dokument otrzymany : " + json.dumps(data))

    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


app.run(port=app_port)

# sudo dapr run --app-port 8010 --app-id subscriber-app --app-protocol http --dapr-http-port 3510 -- ./subscriber/bin/python3 app.py
