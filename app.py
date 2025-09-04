import os

from flask import Flask
from flask_smorest import Api
from resources.task import blp as TaskBlueprint
from resources.user import blp as UserBlueprint
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from db import db


def create_app(db_url=None):
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Todo REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.1.0"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

  jwt = JWTManager(app)
  db.init_app(app)
  migrate = Migrate(app, db)
  api = Api(app)

  # Don't needed after Migrate
  # with app.app_context():
  #     db.create_all()

  api.register_blueprint(TaskBlueprint)
  api.register_blueprint(UserBlueprint)

  return app