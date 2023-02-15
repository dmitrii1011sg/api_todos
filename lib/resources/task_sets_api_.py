from flask import jsonify, request
from flask_restful import Resource

from lib.database_service.db_service import DatabaseService
from lib.parsers.create_set import parser_create_set
from lib.utils.utils import abort_if_user_is_not_auth, abort_if_set_doesnt_exist


class SetsAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self):
        abort_if_user_is_not_auth()
        sets_list = list(map(lambda se: se.shortest_information(), self.database_service.get_all_sets()))
        response = jsonify({
            'sets': sets_list,
            'total': len(sets_list)
        })
        return response

    def post(self):
        abort_if_user_is_not_auth()
        request.get_json(force=True)
        args = parser_create_set.parse_args()
        new_set = self.database_service.create_set(args)
        response = jsonify(new_set)
        return response


class SetAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self, id_set):
        abort_if_user_is_not_auth()
        abort_if_set_doesnt_exist(id_set)
        task_set = self.database_service.get_set_by_id(id_set)
        response = jsonify(task_set.full_information())
        return response


class SetTasksAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self, id_set):
        abort_if_user_is_not_auth()
        abort_if_set_doesnt_exist(id_set)
        tasks = list(map(lambda ta: ta.shortest_information(), self.database_service.get_task_by_set_id(id_set)))
        response = jsonify({
            "tasks": tasks,
            "total": len(tasks)
        })
        return response
