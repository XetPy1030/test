from rest_framework.exceptions import ValidationError


class BaseValidatorForFields(object):
    def __init__(self, fields, validator, message=None):
        self.fields = fields
        self.validator = validator
        self.message = message

    def __call__(self, form, field):
        for field_name in self.fields:
            if not self.validator(form.data.get(field_name)):
                raise ValidationError(self.message)
