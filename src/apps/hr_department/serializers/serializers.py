from rest_framework import serializers

from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.serializers.fields import fields_frontend, fields_backend, date_fields
from apps.hr_department.serializers.reformaters import reformat_fields

fields_frontend_to_backend = {
    key: value for key, value in zip(fields_frontend, fields_backend)
}


def get_field_name(field):
    return fields_frontend_to_backend.get(field, field)


class BaseEmployeeInformationSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data = {
            get_field_name(key): value for key, value in data.items()
        }

        reformat_fields(data)

        return super().to_internal_value(data)


class DraftEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = DraftEmployeeInformation
        fields = '__all__'
        validators = [
            ...
        ]
