from apps.hr_department.validators.base import BaseValidatorForFields
import jwt


def is_jwt_token(token: str):
    try:  # TODO: add secret key
        jwt.decode(token, verify=False, verify_exp=True, verify_nbf=True, verify_iat=True)
    except jwt.PyJWTError:
        return False
    return True


class JwtTokenValidator(BaseValidatorForFields):
    def __init__(self, message=None):
        super().__init__(['jwt_token'], is_jwt_token, 'jwt_token is not valid')


def is_admin(token: str):
    decoded = jwt.decode(token, verify=False)
    return 'admin' in decoded['payload']['resource_access']['account']['roles']


class AdminJwtTokenValidator(BaseValidatorForFields):
    def __init__(self, message=None):
        super().__init__(['jwt_token'], is_admin, 'User is not admin')
