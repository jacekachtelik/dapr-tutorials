import json
import time
import random
import logging
import requests
import os

logging.basicConfig(level=logging.INFO)

base_url = (
    os.getenv("BASE_URL", "http://localhost")
    + ":"
    + os.getenv("DAPR_HTTP_PORT", "3500")
)
PUBSUB_NAME = "documentspubsub"
TOPIC = "documents"
logging.info(
    "Wysyłanie wiadomości na adres: %s, nazwa Pubsub: %s, Temat: %s"
    % (base_url, PUBSUB_NAME, TOPIC)
)

for counter in range(1, 10):
    document = {"documentId": counter}

    # Publish an event/message using Dapr PubSub via HTTP Post
    result = requests.post(
        url="%s/v1.0/publish/%s/%s" % (base_url, PUBSUB_NAME, TOPIC), json=document
    )
    logging.info("Wysłane dane: " + json.dumps(document))

    time.sleep(1)

# sudo dapr run --app-id publisher-http -- ./publisher/bin/python3 app.py
