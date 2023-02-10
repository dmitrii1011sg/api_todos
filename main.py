from data import db_session
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, abort

from data.task_model import Task


app = Flask(__name__)
api = Api(app)


def abort_if_task_doesnt_exist(id):
    db_sess = db_session.create_session()
    task = db_sess.query(Task).filter(Task.id == id).first()
    if not task:
        abort(404, error_code="404", message=f"Task {id} doesn't exist")

class TasksListAPI(Resource):
    def get(self):
        db_sess = db_session.create_session()
        tasks_list = list(map(lambda x: x.shortest_information(), db_sess.query(Task).all()))
        total = len(tasks_list)
        return jsonify({'tasks': tasks_list, 'total': total})

    def post(self):
        json_data = request.get_json(force=True)
        new_task = Task(title=json_data['title'], content=json_data['content'])

        db_sess = db_session.create_session()
        db_sess.add(new_task)
        db_sess.commit()
        return jsonify(new_task.full_information())


class TaskAPI(Resource):
    def get(self, id):
        abort_if_task_doesnt_exist(id)
        db_sess = db_session.create_session()
        task = db_sess.query(Task).filter(Task.id == id).first()
        return jsonify(task.full_information())

    def put(self, id):
        abort_if_task_doesnt_exist(id)
        json_data = request.get_json(force=True)
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id).update(json_data)
        db_sess.commit()
        return jsonify(db_sess.query(Task).filter(Task.id == id).first().full_information())

    def delete(self, id):
        abort_if_task_doesnt_exist(id)
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id).delete()
        db_sess.commit()
        return '', 204


api.add_resource(TasksListAPI, '/api/task/')
api.add_resource(TaskAPI, '/api/task/<int:id>')

if __name__ == '__main__':
    db_session.global_init("database/database.db")
    app.run(debug=True)
