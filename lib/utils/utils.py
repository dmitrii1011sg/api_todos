import flask_login
from flask_restful import abort
from sqlalchemy import and_

from data import db_session
from data.task_model import Task
from data.taskset_model import TaskSet


def abort_if_task_doesnt_exist(id_task: int):
    db_sess = db_session.create_session()
    task = db_sess.query(Task).filter(and_(Task.id == id_task, Task.user_id == flask_login.current_user.id)).first()
    if not task:
        abort(404, status=404, error=f"Task {id_task} doesn't exist")


def abort_if_set_doesnt_exist(id_set: int):
    db_sess = db_session.create_session()
    set = db_sess.query(TaskSet).filter(
        and_(TaskSet.id == id_set, TaskSet.user_id == flask_login.current_user.id)).first()
    if not set:
        abort(404, status=404, error=f"Tasks Set {id_set} doesn't exist")


def abort_if_user_is_not_auth():
    if not flask_login.current_user.is_authenticated:
        abort(404, status=404, error=f"You are not logged in to your account")
