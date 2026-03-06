from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.scheduler import schedule_task
from orchestrator.logger import get_logger

app = FastAPI()

logger = get_logger("Orchestrator")


class Task(BaseModel):

    task_id: str
    payload: dict


@app.get("/")
def root():

    return {"message": "AI Agent Orchestrator Running"}


@app.post("/task")
def submit_task(task: Task):

    task_data = {
        "task_id": task.task_id,
        "payload": task.payload
    }

    schedule_task(task_data)

    logger.info(f"Received task {task.task_id}")

    return {"status": "queued", "task_id": task.task_id}