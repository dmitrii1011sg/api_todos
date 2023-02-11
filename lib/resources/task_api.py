from flask import jsonify, request
from flask_restful import Resource

from data import db_session
from data.task_model import Task
from lib.utils.utils import abort_if_task_doesnt_exist


class TaskAPI(Resource):
    def get(self, id_task):
        abort_if_task_doesnt_exist(id_task)
        db_sess = db_session.create_session()
        task = db_sess.query(Task).filter(Task.id == id_task).first()
        return jsonify(task.full_information())

    def put(self, id_task):
        abort_if_task_doesnt_exist(id_task)
        json_data = request.get_json(force=True)
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id_task).update(json_data)
        db_sess.commit()
        return jsonify(db_sess.query(Task).filter(Task.id == id_task).first().full_information())

    def delete(self, id_task):
        abort_if_task_doesnt_exist(id_task)
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id_task).delete()
        db_sess.commit()
        return '', 204
