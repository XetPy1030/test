from apps.hr_department.validators.base import BaseValidatorForFields


class JwtTokenValidator(BaseValidatorForFields):
    def __init__(self, message=None):
        super().__init__(['jwt_token'], self.is_jwt_token, 'jwt_token is not valid')

    @staticmethod
    def is_jwt_token(token):
        return token.startswith('Bearer ')
