from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import TaskSchema, TaskUpdateSchema, StatusUpdateSchema
from db import tasks

blp = Blueprint("Tasks", __name__, description="Operation on tasks")

@blp.route("/tasks/<int:task_id>")
class TaskManagement(MethodView):
  @blp.response(200, TaskSchema)
  def get(self, task_id):
    try:
      return tasks[task_id]
    except KeyError:
      abort(404, message="Task not found")

  @blp.arguments(TaskUpdateSchema)
  @blp.response(200, TaskSchema)
  def put(self, task_data, task_id):
    new_task = {**task_data, "id": task_id}
    tasks[task_id] = new_task
    return tasks[task_id]


  @blp.arguments(StatusUpdateSchema)
  @blp.response(200, TaskSchema)
  def patch(self, task_data, task_id):
    try:
      tasks[task_id].update(task_data)
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