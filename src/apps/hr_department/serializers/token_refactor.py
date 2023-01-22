import jwt

from config import settings


def jwt_token_check(data):
    if 'jwt_token' in data:
        try:
            jwt.decode(data['jwt_token'], settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            data['jwt_token'] = None
        except jwt.InvalidTokenError:
            data['jwt_token'] = None


def jwt_token_refactor(data):
    # TODO: decode jwt_token and check if it is valid
    data['user_id'] = 111
    data['owner_id'] = 111
    data['full_name'] = 'Иванов Иван Иванович'
