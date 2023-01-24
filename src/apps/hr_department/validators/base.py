from rest_framework.exceptions import ValidationError


class BaseValidatorForFields(object):
    def __init__(self, fields, validator, message=None):
        self.fields = fields
        self.validator = validator
        self.message = message

    def __call__(self, fields):
        for key in self.fields:
            if not self.validator(fields[key]):
                raise ValidationError(self.message)
