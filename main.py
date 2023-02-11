from data import db_session
from flask import Flask
from flask_restful import Api

from lib.resources.task_api import TaskAPI
from lib.resources.tasks_list_api import TasksListAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(TasksListAPI, '/api/task/')
api.add_resource(TaskAPI, '/api/task/<int:id_task>')

if __name__ == '__main__':
    db_session.global_init("database/database.db")
    app.run(debug=True)
