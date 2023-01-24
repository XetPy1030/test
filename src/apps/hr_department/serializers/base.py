from rest_framework import serializers

from apps.hr_department.serializers.fields import fields_frontend_to_backend, fields_backend_to_frontend
from apps.hr_department.serializers.reformaters import reformat_frontend_fields


class BaseEmployeeInformationSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data = {
            self.get_field_backend_name(key): value for key, value in data.items()
        }

        reformat_frontend_fields(data)

        return super().to_internal_value(data)

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #
    #     data = {
    #         self.get_field_frontend_name(key): value for key, value in data.items()
    #     }
    #
    #     # TODO: reformat
    #
    #     return data

    @staticmethod
    def get_field_frontend_name(field):
        return fields_backend_to_frontend.get(field, field)

    @staticmethod
    def get_field_backend_name(field):
        return fields_frontend_to_backend.get(field, field)
