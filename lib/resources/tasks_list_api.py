from flask import jsonify, request
from flask_restful import Resource

from data import db_session
from data.task_model import Task
from lib.database_service.db_service import DatabaseService


class TasksListAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self):
        tasks_list = self.database_service.get_all_tasks()
        total = len(tasks_list)
        return jsonify({'tasks': tasks_list, 'total': total})

    def post(self):
        json_data = request.get_json(force=True)
        new_task = Task(title=json_data['title'],
                        content=json_data['content'],
                        status=json_data['status'],
                        priority=json_data['priority'])

        db_sess = db_session.create_session()
        db_sess.add(new_task)
        db_sess.commit()
        return jsonify(new_task.full_information())
