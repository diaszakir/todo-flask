from flask import Flask, request

app = Flask(__name__)

tasks = {
  1: {
    "id": 1,
    "name": "Read book"
  },
  2: {
    "id": 2,
    "name": "Play FFVII"
  }
}

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
  tasks.append(task_data)
  return {"message": "Task added"}, 201