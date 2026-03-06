import redis
import json
from orchestrator.logger import get_logger

logger = get_logger("Scheduler")

redis_client = redis.Redis(host="redis", port=6379, db=0)

QUEUE = "agent_queue"


def schedule_task(task):

    redis_client.lpush(QUEUE, json.dumps(task))

    logger.info(f"Task scheduled: {task}")