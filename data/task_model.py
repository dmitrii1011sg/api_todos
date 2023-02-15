import datetime
import enum

import sqlalchemy
from .db_session import SqlAlchemyBase


class StatusEnum(enum.Enum):
    DONE = 'DONE'
    PROGRESS = 'PROGRESS'
    NOT_STARTED = 'NOT_STARTED'


class PriorityEnum(enum.Enum):
    LOW = 'LOW',
    MEDIUM = 'MEDIUM',
    HIGH = 'HIGH'


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(150))
    content = sqlalchemy.Column(sqlalchemy.String(2000))
    status = sqlalchemy.Column(sqlalchemy.Enum(StatusEnum), default=None)
    priority = sqlalchemy.Column(sqlalchemy.Enum(PriorityEnum), default=None)
    set_id = sqlalchemy.Column(sqlalchemy.Integer, default=None)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def shortest_information(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_date,
            'status': self.status.name if self.status else None,
            'priority': self.priority.name if self.priority else None,
            'set_id': self.set_id
        }

    def full_information(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'status': self.status.name if self.status else None,
            'priority': self.priority.name if self.priority else None,
            'created_at': self.created_date,
            'set_id': self.set_id
        }
