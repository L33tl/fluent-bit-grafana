import json
import random
import time
from datetime import datetime, timezone

LOG_FILE = "/logs/app.log"

import logging, sys, time, json
logging.basicConfig(
  level=logging.INFO, 
  stream=sys.stdout, 
  format='%%(asctime)s %%(levelname)s %%(message)s'
)
logger = logging.getLogger('app')

def write_log(event, **fields):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "app",
        "event": event,
        **fields,
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")


while True:
    latency = random.randint(20, 400)
    status = random.choice([200, 200, 200, 300, 300, 400, 400, 400, 400, 500])

    write_log(
        "http_request",
        latency_ms=latency,
        status_code=status,
    )

    time.sleep(5)
