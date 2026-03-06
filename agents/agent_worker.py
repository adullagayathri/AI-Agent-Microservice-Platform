import redis
import json
import time

from tasks import process

redis_client = redis.Redis(host="redis", port=6379, db=0)

QUEUE = "agent_queue"
HEARTBEAT = "agent_heartbeat"

AGENT_ID = "agent_1"


def send_heartbeat():

    redis_client.hset(HEARTBEAT, AGENT_ID, time.time())


def run():

    print("Agent started")

    while True:

        send_heartbeat()

        task = redis_client.rpop(QUEUE)

        if task:

            task = json.loads(task)

            process(task)

        else:
            time.sleep(1)


if __name__ == "__main__":
    run()