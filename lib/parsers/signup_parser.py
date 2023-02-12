from flask_restful import reqparse

parser_signup_user = reqparse.RequestParser()
parser_signup_user.add_argument('login', type=str)
parser_signup_user.add_argument('password', type=str)
parser_signup_user.add_argument('name', type=str)
