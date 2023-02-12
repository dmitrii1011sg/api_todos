from flask_restful import reqparse

parser_create_task = reqparse.RequestParser()
parser_create_task.add_argument('title', type=str)
parser_create_task.add_argument('content', type=str)
parser_create_task.add_argument('status', type=str)
parser_create_task.add_argument('priority', type=str)
parser_create_task.add_argument('set_id', type=int)
