from flask import jsonify, request
from flask_restful import Resource

from lib.database_service.db_service import DatabaseService
from lib.parsers.create_set import parser_create_set
from lib.utils.utils import abort_if_user_is_not_auth


class TaskSetsAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self):
        abort_if_user_is_not_auth()
        sets_list = self.database_service.get_all_sets()
        total = len(sets_list)
        return jsonify({'sets': sets_list, 'total': total})

    def post(self):
        abort_if_user_is_not_auth()
        request.get_json(force=True)
        args = parser_create_set.parse_args()
        new_set = self.database_service.create_set(args)
        return jsonify(new_set)
