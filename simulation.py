import requests
import time
import uuid

URL = "http://localhost:8000/task"

while True:

    task = {
        "task_id": str(uuid.uuid4()),
        "payload": {"data": "AI processing"}
    }

    requests.post(URL, json=task)

    print("Task sent")

    time.sleep(3)