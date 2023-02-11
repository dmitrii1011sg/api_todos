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

    def get_all_sets(self):
        db_sess = db_session.create_session()
        sets_list = list(map(lambda x: x.shortest_information(), db_sess.query(Category).all()))
        return sets_list
