from flask_restful import Resource, reqparse, fields, marshal_with
from models import UserModel, db
from werkzeug.security import generate_password_hash

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True)
user_args.add_argument('email', type=str, required=True)
user_args.add_argument('password', type=str, required=True)

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        return UserModel.query.all()

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        hashed_password = generate_password_hash(args["password"])
        user = UserModel(
            name=args["name"],
            email=args["email"],
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user, 201