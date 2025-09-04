from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from db import db
from schemas import UserSchema
from models import UserModel

blp = Blueprint("Users", __name__, description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="User with that username already exists.")

        user = UserModel(username=user_data["username"], password=pbkdf2_sha256.hash(user_data["password"]))

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201