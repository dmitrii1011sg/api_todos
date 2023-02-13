import os

import flask_login
from dotenv import load_dotenv
from flask_login import LoginManager, login_required, logout_user

from data import db_session
from flask import Flask
from flask_restful import Api

from data.user_model import User
from lib.resources.task_api_ import TasksAPI, TaskAPI
from lib.resources.task_sets_api_ import SetsAPI, SetAPI, SetTasksAPI
from lib.resources.users_api import AuthAPI, SignUpAPI

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
api.add_resource(TasksAPI, '/api/task/')
api.add_resource(TaskAPI, '/api/task/<int:id_task>')
api.add_resource(SetsAPI, '/api/task-sets/')
api.add_resource(SetAPI, '/api/task-sets/<int:id_set>')
api.add_resource(SetTasksAPI, '/api/task-sets/<int:id_set>/tasks')

if __name__ == '__main__':
    db_session.global_init("database/database.db")
    app.run(debug=True)
