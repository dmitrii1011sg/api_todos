import flask_login
from sqlalchemy import and_

from data import db_session
from data.taskset_model import TaskSet
from data.task_model import Task
from data.user_model import User


# noinspection PyMethodMayBeStatic
class DatabaseService:
    def get_user(self, login: str, password: str):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == login).first()
        return user if user and user.check_password(password) else False

    def create_user(self, login: str, name: str, password: str):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == login).first()
        if user:
            return False
        new_user = User(name=name if name else login, login=login)
        new_user.set_password(password)
        db_sess.add(new_user)
        db_sess.commit()
        return db_sess.query(User).filter(User.login == login).first()

    def get_all_tasks(self):
        db_sess = db_session.create_session()
        return db_sess.query(Task).filter(Task.user_id == flask_login.current_user.id).all()

    def create_task(self, param: dict) -> dict:
        new_task = Task(title=param['title'],
                        content=param['content'],
                        status=param['status'],
                        priority=param['priority'],
                        set_id=param.get('set_id'),
                        user_id=flask_login.current_user.id)

        db_sess = db_session.create_session()
        db_sess.add(new_task)
        db_sess.commit()
        return new_task.full_information()

    def get_task_by_id(self, id_task: int):
        db_sess = db_session.create_session()
        return db_sess.query(Task).filter(and_(Task.id == id_task, Task.user_id == flask_login.current_user.id)).first()

    def update_task_by_id(self, id_task: int, param: dict):
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(and_(Task.id == id_task, Task.user_id == flask_login.current_user.id)).update(param)
        db_sess.commit()

    def delete_task_by_id(self, id_task: int):
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(and_(Task.id == id_task, Task.user_id == flask_login.current_user.id)).delete()
        db_sess.commit()

    def get_all_sets(self):
        db_sess = db_session.create_session()
        return db_sess.query(TaskSet).filter(TaskSet.user_id == flask_login.current_user.id).all()

    def get_set_by_id(self, id_set: int):
        db_sess = db_session.create_session()
        return db_sess.query(TaskSet).filter(and_(TaskSet.id == id_set,
                                                  TaskSet.user_id == flask_login.current_user.id)).first()

    def create_set(self, param: dict) -> dict:
        new_set = TaskSet(title=param['title'], description=param['description'], user_id=flask_login.current_user.id)

        db_sess = db_session.create_session()
        db_sess.add(new_set)
        db_sess.commit()
        return new_set.full_information()

    def get_task_by_set_id(self, set_id: int):
        db_sess = db_session.create_session()
        return db_sess.query(Task).filter(and_(Task.set_id == set_id,
                                               Task.user_id == flask_login.current_user.id)).all()
