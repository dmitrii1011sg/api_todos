from flask import jsonify, request
from flask_restful import Resource

from lib.database_service.db_service import DatabaseService
from lib.parsers.create_task_parser import parser_create_task
from lib.utils.utils import abort_if_user_is_not_auth, abort_if_task_doesnt_exist


class TasksAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self):
        abort_if_user_is_not_auth()
        tasks_list = self.database_service.get_all_tasks()
        total = len(tasks_list)
        return jsonify({'tasks': tasks_list, 'total': total})

    def post(self):
        abort_if_user_is_not_auth()
        request.get_json(force=True)
        args = parser_create_task.parse_args()
        new_task = self.database_service.create_task(args)
        return jsonify(new_task)


class TaskAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self, id_task):
        abort_if_user_is_not_auth()
        abort_if_task_doesnt_exist(id_task)
        task = self.database_service.get_task_by_id(id_task)
        return jsonify(task.full_information())

    def put(self, id_task):
        abort_if_user_is_not_auth()
        abort_if_task_doesnt_exist(id_task)
        json_data = request.get_json(force=True)
        self.database_service.update_task_by_id(id_task, json_data)
        return jsonify(self.database_service.get_task_by_id(id_task).full_information())

    def delete(self, id_task):
        abort_if_user_is_not_auth()
        abort_if_task_doesnt_exist(id_task)
        self.database_service.delete_task_by_id(id_task)
        return '', 200
