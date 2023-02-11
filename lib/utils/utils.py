from datetime import datetime

from flask_restful import abort

from data import db_session
from data.task_model import Task
from data.taskset_model import TaskSet


def abort_if_task_doesnt_exist(id_task):
    db_sess = db_session.create_session()
    task = db_sess.query(Task).filter(Task.id == id_task).first()
    if not task:
        abort(404, status=404, error=f"Task {id_task} doesn't exist")


def abort_if_set_doesnt_exist(id_set):
    db_sess = db_session.create_session()
    set = db_sess.query(TaskSet).filter(TaskSet.id == id_set).first()
    if not set:
        abort(404, status=404, error=f"Tasks Set {id_set} doesn't exist")
