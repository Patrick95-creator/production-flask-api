from flask import Flask
from flask_restful import Api
from models import db
from resources.users import Users
from resources.user import User
from resources.login import Login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
api = Api(app)

api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')
api.add_resource(Login, '/api/login')
@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)