from apps.hr_department.validators.base import BaseValidatorForFields


class NotMeValidator(BaseValidatorForFields):  # TODO
    def __init__(self):
        super().__init__(['user_id'], self.check, 'User can not be owner')

    @staticmethod
    def check(data):
        return data['user_id'] == data['owner_id']
