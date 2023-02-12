from flask_restful import reqparse

parser_auth_user = reqparse.RequestParser()
parser_auth_user.add_argument('login', type=str)
parser_auth_user.add_argument('password', type=str)
