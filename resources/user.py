from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models import UserModel, db

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True)
user_args.add_argument('email', type=str, required=True)

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user

    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user

    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        db.session.delete(user)
        db.session.commit()
        return user, 200