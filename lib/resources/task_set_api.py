from flask import jsonify
from flask_restful import Resource

from lib.database_service.db_service import DatabaseService
from lib.utils.utils import abort_if_set_doesnt_exist, abort_if_user_is_not_auth


class TaskSetAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self, id_set):
        abort_if_user_is_not_auth()
        abort_if_set_doesnt_exist(id_set)
        set = self.database_service.get_set_by_id(id_set)
        return jsonify(set.full_information())


class SetAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self, id_set):
        abort_if_user_is_not_auth()
        abort_if_set_doesnt_exist(id_set)
        tasks = self.database_service.get_task_by_set_id(id_set)
        return jsonify({"tasks": tasks, "total": len(tasks)})
