import sqlalchemy
from .db_session import SqlAlchemyBase


class TaskSet(SqlAlchemyBase):
    __tablename__ = 'taskset'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))
    description = sqlalchemy.Column(sqlalchemy.String(400), nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def shortest_information(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def full_information(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
