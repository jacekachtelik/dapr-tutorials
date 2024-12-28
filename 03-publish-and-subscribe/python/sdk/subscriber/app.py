from flask import Flask, request, jsonify
from cloudevents.http import from_http
import json
import os

app = Flask(__name__)

app_port = os.getenv("APP_PORT", "56001")


# Register Dapr pub/sub subscriptions
@app.route("/dapr/subscribe", methods=["GET"])
def subscribe():
    subscriptions = [
        {"pubsubname": "orderpubsub", "topic": "documents", "route": "documents"}
    ]
    print("Dapr pub/sub is zasubskrybowany do: " + json.dumps(subscriptions))
    return jsonify(subscriptions)


# Dapr subscription in /dapr/subscribe sets up this route
@app.route("/documents", methods=["POST"])
def documents_subscriber():
    event = from_http(request.headers, request.get_data())
    print("Subskrybent otrzymał zdarzenie : %s" % event.data["documentId"], flush=True)
    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


app.run(port=app_port)

# sudo dapr run --app-id subscriber-sdk --app-port 6002 --resources-path $HOME/.dapr/components/ -- ./subscriber/bin/uvicorn app:app
# sudo dapr run --app-id subscriber-sdk --app-port 6002 --resources-path $HOME/.dapr/components/ -- ./subscriber/bin/python3 app.py
# sudo dapr run --app-id subscriber-sdk --app-port 6002 --resources-path ../../../myComponents/ -- ./subscriber/bin/python3 app.py
