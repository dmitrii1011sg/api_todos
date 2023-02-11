from flask import jsonify, request
from flask_restful import Resource

from data import db_session
from data.task_model import Task


class TaskSetAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass
