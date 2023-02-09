import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    title = sqlalchemy.Column(sqlalchemy.String(150))
    content = sqlalchemy.Column(sqlalchemy.String)

    def shortest_information(self):
        return {
            'title': self.title,
            'created_at': self.created_date
        }

    def full_information(self):
        return {
            'title': self.title,
            'content': self.content,
            'created_at': self.created_date,
        }
