from flask import jsonify, request
from flask_restful import Resource

from data import db_session
from data.category_model import Category
from data.task_model import Task
from lib.database_service.db_service import DatabaseService


class TaskSetsAPI(Resource):
    def __init__(self):
        self.database_service = DatabaseService()

    def get(self):
        sets_list = self.database_service.get_all_sets()
        total = len(sets_list)
        return jsonify({'sets': sets_list, 'total': total})

    def post(self):
        json_data = request.get_json(force=True)
        new_set = Category(name=json_data['name'], description=json_data['description'])

        db_sess = db_session.create_session()
        db_sess.add(new_set)
        db_sess.commit()
        return jsonify(new_set.full_information())
