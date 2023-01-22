# lib for checking jwt token is valid
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler

def check_jwt_token(token):
    jwt_decode_handler(token)


def jwt_token_refactor(data):
    ...
