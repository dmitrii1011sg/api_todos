import datetime

import sqlalchemy
from .db_session import SqlAlchemyBase


class TaskSet(SqlAlchemyBase):
    __tablename__ = 'taskset'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(20))
    description = sqlalchemy.Column(sqlalchemy.String(400), nullable=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def shortest_information(self):
        return {
            'id': self.id,
            'name': self.title
        }

    def full_information(self):
        return {
            'id': self.id,
            'name': self.title,
            'description': self.description
        }
