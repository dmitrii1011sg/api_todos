import flask_login
from flask import jsonify, request
from flask_restful import Resource, abort

from lib.database_service.db_service import DatabaseService
from lib.parsers.auth_user_parser import parser_auth_user
from lib.utils.utils import abort_if_task_doesnt_exist


class AuthAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self):
        return jsonify(flask_login.current_user.get_data() if flask_login.current_user.is_authenticated else None)

    def post(self):
        request.get_json(force=True)
        args = parser_auth_user.parse_args()
        if args['login'] and args['password']:
            user = self.database_service.check_user(args['login'], args['password'])
            flask_login.login_user(user)
            return jsonify(user.get_data())
        abort(404,  status=404, error=f"Login or password invalid")
