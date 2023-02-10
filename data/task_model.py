import datetime
import enum

import sqlalchemy
from .db_session import SqlAlchemyBase


class StatusEnum(enum.Enum):
    DONE = 'DONE'
    PROGRESS = 'PROGRESS'
    NOT_STARTED = 'NOT_STARTED'


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    title = sqlalchemy.Column(sqlalchemy.String(150))
    content = sqlalchemy.Column(sqlalchemy.String)
    status = sqlalchemy.Column(sqlalchemy.Enum(StatusEnum))

    def shortest_information(self):
        return {
            'title': self.title,
            'created_at': self.created_date,
            'status': self.status.name
        }

    def full_information(self):
        return {
            'title': self.title,
            'content': self.content,
            'status': self.status.name,
            'created_at': self.created_date,
        }
