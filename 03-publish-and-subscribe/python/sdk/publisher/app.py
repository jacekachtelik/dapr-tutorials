from dapr.clients import DaprClient
import json
import time
import logging

logging.basicConfig(level=logging.INFO)

with DaprClient() as client:
    for counter in range(1, 10):
        document = {"documentId": counter}

        # Publish event/message using Dapr PubSub
        result = client.publish_event(
            pubsub_name="documentspubsub",
            topic_name="documents",
            data=json.dumps(document),
            data_content_type="application/json",
        )

        logging.info("Wysłane dane: " + json.dumps(document))
        time.sleep(1)

# sudo dapr run --app-id publisher-sdk --resources-path $HOME/.dapr/components/ -- ./publisher/bin/python3 app.py
