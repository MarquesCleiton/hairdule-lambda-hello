import json
import os
from datetime import datetime, timezone


def handler(event, context):
    body = {
        "message": "Hello World!",
        "app": os.getenv("APP_NAME", "hairdule"),
        "stage": os.getenv("STAGE", "homol"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request_id": getattr(context, "aws_request_id", None),
        "event_echo": event,
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
