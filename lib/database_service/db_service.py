from data import db_session
from data.taskset_model import TaskSet
from data.task_model import Task
from data.user_model import User


class DatabaseService:
    def check_user(self, login: str, password: str):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == login).first()
        if user and user.check_password(password):
            return user
        return False

    def create_user(self, login: str, name: str, password: str):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == login).first()
        if not user:
            new_user = User(name=name if name else login, login=login)
            print(new_user)
            new_user.set_password(password)
            db_sess.add(new_user)
            db_sess.commit()
            return user.get_data()
        return False


    def get_all_tasks(self):
        db_sess = db_session.create_session()
        tasks_list = list(map(lambda x: x.shortest_information(), db_sess.query(Task).all()))
        return tasks_list

    def create_task(self, param: dict) -> dict:
        new_task = Task(title=param['title'],
                        content=param['content'],
                        status=param['status'],
                        priority=param['priority'],
                        set_id=param.get('set_id'))

        db_sess = db_session.create_session()
        db_sess.add(new_task)
        db_sess.commit()
        return new_task.full_information()

    def get_task_by_id(self, id_task: int):
        db_sess = db_session.create_session()
        task = db_sess.query(Task).filter(Task.id == id_task).first()
        return task

    def update_task_by_id(self, id_task: int, param: dict):
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id_task).update(param)
        db_sess.commit()

    def delete_task_by_id(self, id_task: int):
        db_sess = db_session.create_session()
        db_sess.query(Task).filter(Task.id == id_task).delete()
        db_sess.commit()

    def get_all_sets(self):
        db_sess = db_session.create_session()
        sets_list = list(map(lambda x: x.shortest_information(), db_sess.query(TaskSet).all()))
        return sets_list

    def get_set_by_id(self, id_set: int):
        db_sess = db_session.create_session()
        set = db_sess.query(TaskSet).filter(TaskSet.id == id_set).first()
        return set

    def create_set(self, param: dict) -> dict:
        new_set = TaskSet(name=param['name'], description=param['description'])

        db_sess = db_session.create_session()
        db_sess.add(new_set)
        db_sess.commit()
        return new_set.full_information()

    def get_task_by_set_id(self, set_id: int):
        db_sess = db_session.create_session()
        tasks_list = list(map(lambda x: x.shortest_information(), db_sess.query(Task)
                              .filter(Task.set_id == set_id).all()))
        return tasks_list
