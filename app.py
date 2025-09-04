import os

from flask import Flask, jsonify
from flask_smorest import Api
from resources.task import blp as TaskBlueprint
from resources.user import blp as UserBlueprint
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from db import db
from models import UserModel
from models import BlocklistModel


def create_app(db_url=None):
  app = Flask(__name__) # Initialize flask application

  # app configurations
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

  # JWT loaders
  @jwt.token_in_blocklist_loader
  def check_if_token_in_blocklist(jwt_header, jwt_payload):
      jti = jwt_payload["jti"]
      token = BlocklistModel.query.get(jti)
      return token is not None

  @jwt.additional_claims_loader
  def add_claims_to_jwt(identity):
      user = UserModel.query.get_or_404(identity)
      if user.id == 1:
          return {'is_admin': True}
      return {'is_admin': False}

  @jwt.expired_token_loader
  def expired_token_callback(jwt_header, jwt_payload):
      return jsonify(
          {
              "message": "The token has expired",
              "error": "token_expired"
          }
      ), 401

  @jwt.invalid_token_loader
  def invalid_token_callback(error):
      return jsonify(
          {
              "message": "Signature verification failed",
              "error": "invalid_token"
          }
      ), 401

  @jwt.unauthorized_loader
  def missing_token_callback(error):
      return jsonify(
          {
              "description": "Request does not contain an access token",
              "error": "authorization_required"
          }
      ), 401

  @jwt.needs_fresh_token_loader
  def token_not_fresh_callback(jwt_header, jwt_payload):
      return (
          jsonify(
              {
                  "description": "The token is not fresh.",
                  "error": "fresh_token_required",
              }
          ),
          401,
      )

  # Don't needed after Migrate
  # with app.app_context():
  #     db.create_all()

  # Adding to blueprint
  api.register_blueprint(TaskBlueprint)
  api.register_blueprint(UserBlueprint)

  return app