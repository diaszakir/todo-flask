from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from schemas import TaskSchema, TaskUpdateSchema, StatusUpdateSchema
from db import db
from models import TaskModel

blp = Blueprint("Tasks", __name__, description="Operation on tasks")

@blp.route("/tasks/<int:task_id>")
class TaskManagement(MethodView):
  @jwt_required()
  @blp.response(200, TaskSchema)
  def get(self, task_id):
    task = TaskModel.query.get_or_404(task_id)
    return task

  @blp.arguments(TaskUpdateSchema)
  @blp.response(200, TaskSchema)
  def put(self, task_data, task_id):
    task = TaskModel.query.get(task_id)
    if task:
        task.name = task_data["name"]
        task.status = task_data["status"]
    else:
        task = TaskModel(id=task_id, **task_data)

    db.session.add(task)
    db.session.commit()

    return task

  @blp.arguments(StatusUpdateSchema)
  @blp.response(200, TaskSchema)
  def patch(self, task_data, task_id):
    task = TaskModel.query.get(task_id)
    if task:
        task.status = task_data["status"]
    else:
        task = TaskModel(id=task_id, **task_data)

    db.session.add(task)
    db.session.commit()

    return task

  @jwt_required(fresh=True) # Must be fresh token, refresh not accepted
  def delete(self, task_id):
    jwt = get_jwt()
    if not jwt.get('is_admin'): # checking for admin
        abort(401, message="Admin privilege required.")
    task = TaskModel.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return {"message": "Task deleted"}


@blp.route("/tasks")
class TaskCreate(MethodView):
  @jwt_required()
  @blp.response(200, TaskSchema(many=True))
  def get(self):
    return TaskModel.query.all()

  @jwt_required(fresh=True)
  @blp.arguments(TaskSchema)
  @blp.response(201, TaskSchema)
  def post(self, task_data):
    task = TaskModel(**task_data)
    try:
        db.session.add(task)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="An error while inserting a task")
    return task