from flask import Flask, request, jsonify
import json
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app_port = os.getenv("APP_PORT", "6001")

PUBSUB_NAME = "documentspubsub"
TOPIC = "documents"
logging.info("Obieranie wiadomości z Pubsub: %s, Temat: %s" % (PUBSUB_NAME, TOPIC))


# Register Dapr pub/sub subscriptions
@app.route("/dapr/subscribe", methods=["GET"])
def subscribe():
    subscriptions = [{"pubsubname": PUBSUB_NAME, "topic": TOPIC, "route": TOPIC}]

    message = "Dapr pub/sub is zasubskrybowany do: " + json.dumps(subscriptions)
    print(message)
    logging.info(message)

    return jsonify(subscriptions)


# Dapr subscription in /dapr/subscribe sets up this route
@app.route("/documents", methods=["POST"])
def documents_subscriber():
    document = request.json

    message = "Subskrybent otrzymał: " + json.dumps(document)

    print(message, flush=True)
    logging.info(message)

    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


app.run(port=app_port)

# sudo dapr run --app-id subscriber-http --app-port 6021 -- ./subscriber/bin/python3 app.py --port 6002
