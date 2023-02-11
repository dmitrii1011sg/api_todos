from flask import jsonify, request
from flask_restful import Resource

from lib.database_service.db_service import DatabaseService
from lib.utils.utils import abort_if_task_doesnt_exist


class TaskAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self, id_task):
        abort_if_task_doesnt_exist(id_task)
        task = self.database_service.get_task_by_id(id_task)
        return jsonify(task.full_information())

    def put(self, id_task):
        abort_if_task_doesnt_exist(id_task)
        json_data = request.get_json(force=True)
        self.database_service.update_task_by_id(id_task, json_data)
        return jsonify(self.database_service.get_task_by_id(id_task).full_information())

    def delete(self, id_task):
        abort_if_task_doesnt_exist(id_task)
        self.database_service.delete_task_by_id(id_task)
        return '', 204
