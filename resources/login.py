from flask_restful import Resource, reqparse
from models import UserModel
from werkzeug.security import check_password_hash

login_args = reqparse.RequestParser()
login_args.add_argument('email', type=str, required=True)
login_args.add_argument('password', type=str, required=True)

class Login(Resource):
    def post(self):
        args = login_args.parse_args()

        user = UserModel.query.filter_by(email=args["email"]).first()

        if not user:
            return {"message": "User not found"}, 404

        if not check_password_hash(user.password, args["password"]):
            return {"message": "Wrong password"}, 401

        return {
            "message": "Login successful",
            "user_id": user.id
        }, 200