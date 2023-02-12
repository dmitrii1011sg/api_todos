from flask import jsonify, request
from flask_restful import Resource

from data import db_session
from data.task_model import Task
from lib.database_service.db_service import DatabaseService
from lib.parsers.create_task_parser import parser_create_task
from lib.utils.utils import abort_if_user_is_not_auth


class TasksListAPI(Resource):
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
