import time

def process(task):

    print(f"Processing task {task['task_id']}")

    # simulate AI work
    time.sleep(2)

    result = {
        "task_id": task["task_id"],
        "status": "completed"
    }

    print(result)

    return result