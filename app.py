from flask import Flask
from flask_smorest import Api
from resources.task import blp as TaskBlueprint

def create_app():
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Todo REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.1.0"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

  api = Api(app)

  api.register_blueprint(TaskBlueprint)

  return app