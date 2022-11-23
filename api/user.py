from flask import request
from flask_restful import abort
from flask_restful import Resource

from fake_db import FAKE_DB
from serializers.user import UserSchema
from services.utils import get_objects

# from models.user import UserInfo


class ListUsers(Resource):
    def get(self):
        return get_objects('User')


class CreateUser(Resource):
    def post(self):
        args = request.json
        new_user = UserSchema().dump(args)
        FAKE_DB.append(new_user)
        return new_user, 200


class User(Resource):
    def get(self, user_id):
        for user in get_objects('User'):
            if user['id'] == int(user_id):
                return user
        abort(404, message="user {} doesn't exist".format(user_id))

    def delete(self, user_id):
        for user in get_objects('User'):
            if user['id'] == int(user_id):
                user.update({
                    'delete': True
                })
                return user
        abort(404, message="user {} doesn't exist".format(user_id))

    def put(self, user_id):
        args = request.json
        for user in get_objects('User'):
            if user['id'] == int(user_id):
                user.update(args)
                return user
        abort(404, message="user {} doesn't exist".format(user_id))