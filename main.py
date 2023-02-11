from data import db_session
from flask import Flask
from flask_restful import Api

from lib.resources.task_api import TaskAPI
from lib.resources.task_set_api import TaskSetAPI
from lib.resources.task_sets_api import TaskSetsAPI
from lib.resources.tasks_list_api import TasksListAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(TasksListAPI, '/api/task/')
api.add_resource(TaskAPI, '/api/task/<int:id_task>')
api.add_resource(TaskSetsAPI, '/api/task-sets/')
api.add_resource(TaskSetAPI, '/api/task-sets/<int:id_set>')

if __name__ == '__main__':
    db_session.global_init("database/database.db")
    app.run(debug=True)
