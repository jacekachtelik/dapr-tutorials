# Skrypt wysyła wiadomość do Dapr-a.

import os
import json
import time
import logging
import requests

logging.basicConfig(level=logging.INFO)

base_url = (
    os.getenv("BASE_URL", "http://localhost")
    + ":"
    + os.getenv("DAPR_HTTP_PORT", "3515")
)


TOPIC = "documents"

logging.info("Publikowanie na adres: {}, Topic: {} ".format(base_url, TOPIC))

headers = {"dapr-app-id": "subscriber-app", "content-type": "application/json"}

for counter in range(1, 20):

    document = {"documentId": counter}
    url = "{}/{}".format(base_url, TOPIC)

    logging.debug("Url: {}".format(url))
    print("Url: {}".format(url))

    result = requests.post(url=url, data=json.dumps(document), headers=headers)

    logging.info("Wysłany dokument: " + json.dumps(document))
    print("Wysłany dokument: " + json.dumps(document))

    time.sleep(1)

# sudo dapr run --app-id publisher-app --app-protocol http --dapr-http-port 3515 -- ./publisher/bin/python3 app.py
