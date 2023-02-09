import os

from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_restful import Resource, Api

load_dotenv()

app = Flask(__name__)
api = Api(app)


class Tasks(Resource):
    def get(self):
        return jsonify({'hello': 'get'})

    def post(self):
        return jsonify({'hello': 'post'})

class Task(Resource):
    def get(self, id):
        return jsonify({'Task': 'get'})

    def put(self, id):
        return jsonify({'Task': 'put'})

    def delete(self, id):
        return jsonify({'Task': 'delete'})


api.add_resource(Tasks, '/api/task/')
api.add_resource(Task, '/api/task/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
