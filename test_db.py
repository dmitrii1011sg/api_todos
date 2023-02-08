from data.data import db_session
from data.data.tast_model import Task

db_session.global_init("database/database.db")
db_sess = db_session.create_session()
task = Task(title='asd', content="asddanjsnoa")
db_sess.add(task)
db_sess.commit()
