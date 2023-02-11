import sqlalchemy
from .db_session import SqlAlchemyBase


class TaskSet(SqlAlchemyBase):
    __tablename__ = 'taskset'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))
    description = sqlalchemy.Column(sqlalchemy.String(400), nullable=True)

    def shortest_information(self):
        return {
            'name': self.name
        }

    def full_information(self):
        return {
            'name': self.name,
            'description': self.description
        }
