from flask import jsonify, request
from flask_restful import Resource, Api
from App.Models import User


def login(app, db):

    api = Api(app)

    def saveToDB(objectToSave):
        db.session.add(objectToSave)
        db.session.commit()

    class Login(Resource):

        def get(self):
            userName = request.args.get('userName', None)
            passWord = request.args.get('passWord', None)

            if userName and passWord:
                userInDB = User.query.filter_by(user_name=userName,
                    password=passWord).first()
                if userInDB:
                    return jsonify(success="welcome {}!".format(userName))
                return jsonify(error="failed login")
            else:
                return jsonify(error="username and password is required")

        def post(self):
            userName, passWord = None, None
            x = request.get_json()
            if 'userName' not in x and 'passWord' not in x:
                return jsonify(error="username and password is required")

            userName = x['userName']
            passWord = x['passWord']
            user = User.query.filter_by(
                user_name=userName, password=passWord).first()
            if user is None:
                user = User(userName, passWord)
                saveToDB(user)
                return jsonify(success="user created")
            else:
                return jsonify(success="user name is taken, try again")

    api.add_resource(Login, "/api/login")
