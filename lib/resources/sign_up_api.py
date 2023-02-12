import flask_login
from flask import jsonify, request
from flask_restful import Resource, abort

from lib.database_service.db_service import DatabaseService
from lib.parsers.signup_parser import parser_signup_user


class SignUpAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def post(self):
        request.get_json(force=True)
        args = parser_signup_user.parse_args()
        if args['login'] and args['password']:
            user = self.database_service.create_user(args['login'], args['name'], args['password'])
            if user:
                flask_login.login_user(user)
                return jsonify(user.get_data())
            else:
                abort(404,  status=404, error=f"Something went wrong")
