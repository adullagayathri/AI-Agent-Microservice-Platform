import redis
import time
from orchestrator.logger import get_logger

logger = get_logger("HealthMonitor")

redis_client = redis.Redis(host="redis", port=6379, db=0)

HEARTBEAT_KEY = "agent_heartbeat"


def monitor():

    while True:

        agents = redis_client.hgetall(HEARTBEAT_KEY)

        for agent, timestamp in agents.items():

            last_seen = float(timestamp)

            if time.time() - last_seen > 10:
                logger.warning(f"Agent {agent.decode()} might be down")

        time.sleep(5)