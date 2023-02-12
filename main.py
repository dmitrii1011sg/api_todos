import os

import flask_login
from dotenv import load_dotenv
from flask_login import LoginManager, login_required, logout_user

from data import db_session
from flask import Flask
from flask_restful import Api

from data.user_model import User
from lib.resources.auth_api import AuthAPI
from lib.resources.sign_up_api import SignUpAPI
from lib.resources.task_api import TaskAPI
from lib.resources.task_set_api import TaskSetAPI, SetAPI
from lib.resources.task_sets_api import TaskSetsAPI
from lib.resources.tasks_list_api import TasksListAPI

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('TOKEN')
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    return flask_login.current_user


api.add_resource(AuthAPI, '/api/auth/')
api.add_resource(SignUpAPI, '/api/signup/')
api.add_resource(TasksListAPI, '/api/task/')
api.add_resource(TaskAPI, '/api/task/<int:id_task>')
api.add_resource(TaskSetsAPI, '/api/task-sets/')
api.add_resource(TaskSetAPI, '/api/task-sets/<int:id_set>')
api.add_resource(SetAPI, '/api/task-sets/<int:id_set>/tasks')

if __name__ == '__main__':
    db_session.global_init("database/database.db")
    app.run(debug=True)
