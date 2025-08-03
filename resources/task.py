from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import tasks

blp = Blueprint("Tasks", __name__, description="Operation on tasks")

@blp.route("/tasks/<int:task_id>")
class TaskManagement(MethodView):
  def get(self, task_id):
    try:
      return tasks[task_id]
    except KeyError:
      abort(404, message="Task not found")


  def delete(self, task_id):
    try:
      del tasks[task_id]
      return {"message": "Task deleted"}
    except KeyError:
      abort(404, message="Task not found")


@blp.route("/tasks")
class TaskCreate(MethodView):
  def get(self):
    return list(tasks.values())


  def post(self):
    task_data = request.get_json()
    for task in tasks.values():
      if task_data["name"] == task["name"]:
        abort(400, message="Task already exists")
    task_id = len(tasks) + 1
    task = {**task_data, "id": task_id}
    tasks[task_id] = task
    return task