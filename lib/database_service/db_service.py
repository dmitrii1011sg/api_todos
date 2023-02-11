from data import db_session
from data.category_model import Category
from data.task_model import Task


class DatabaseService:
    def __init__(self):
        pass

    def get_all_tasks(self):
        db_sess = db_session.create_session()
        tasks_list = list(map(lambda x: x.shortest_information(), db_sess.query(Task).all()))
        return tasks_list

    def get_task_by_id(self, id_task):
        db_sess = db_session.create_session()
        task = db_sess.query(Task).filter(Task.id == id_task).first()
        return task

    def update_task_by_id(self, id_task, param):
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id_task).update(param)
        db_sess.commit()

    def delete_task_by_id(self, id_task):
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id_task).delete()
        db_sess.commit()

    def get_all_sets(self):
        db_sess = db_session.create_session()
        sets_list = list(map(lambda x: x.shortest_information(), db_sess.query(Category).all()))
        return sets_list
