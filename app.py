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
  if "name" not in task_data or "status" not in task_data:
    return {"message": "Ensure 'name' and 'status' included"}, 400
  task_id = len(tasks) + 1
  new_task = {**task_data, "id": task_id}
  tasks[task_id] = new_task
  return {"message": "Task added", "task": new_task}, 201


@app.put("/tasks/<int:task_id>")
def update_task(task_id):
  task_data = request.get_json()
  if not task_data or "status" not in task_data or "name" not in task_data:
    return {"message": "Invalid request"}, 400
  
  if task_id in tasks:
    tasks[task_id].update(task_data)
    return tasks[task_id]
  
  new_task = {**task_data, "id": task_id}
  tasks[task_id] = new_task
  return tasks[task_id]


@app.patch("/tasks/<int:task_id>")
def update_task_status(task_id):
  if task_id in tasks:
    task_data = request.get_json()
    if not task_data or "status" not in task_data:
      return {"message": "Invalid request"}, 400
    tasks[task_id].update(task_data)
    return tasks[task_id]
  return {"message": "Task not found"}, 404


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
  if task_id in tasks:
    del tasks[task_id]
    return {"message": "Task deleted"}, 200
  return {"message": "Task not found"}, 404