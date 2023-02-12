from flask_restful import reqparse

parser_create_set = reqparse.RequestParser()
parser_create_set.add_argument('name', type=str)
parser_create_set.add_argument('description', type=str)
