from flask import Flask, request

app = Flask(__name__)

tasks = {}

@app.get("/tasks")
def get_all_tasks():
  return {"tasks": list(tasks.values())}


@app.get("/tasks/<int:task_id>")
def exact_task(task_id):
  if task_id in tasks:
    return tasks[task_id]
  return {"message": "Task not found"}, 404


@app.post("/tasks")
def add_new_task():
  task_data = request.get_json()
  task_id = len(tasks) + 1
  new_task = {**task_data, "id": task_id}
  tasks[task_id] = new_task
  return {"message": "Task added", "task": new_task}, 201