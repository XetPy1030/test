from apps.hr_department.validators.base import BaseValidatorForFields


class RequiredFieldsValidator(BaseValidatorForFields):
    def __init__(self, fields, message=None):
        super().__init__(fields, self.is_required, message)

    @staticmethod
    def is_required(value):
        if value is None:
            return False
        return True
