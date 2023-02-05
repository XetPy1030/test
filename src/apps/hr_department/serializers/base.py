import base64
import os
from io import BytesIO

from PIL import Image
from rest_framework import serializers

from apps.hr_department.serializers.utils.fields import fields_frontend_to_backend, fields_backend_to_frontend
from apps.hr_department.serializers.utils.reformaters import reformat_frontend_fields


class BaseSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data = {
            self.get_field_backend_name(key): value for key, value in data.items()
        }

        reformat_frontend_fields(data)

        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
    
        data = {
            self.get_field_frontend_name(key): value for key, value in data.items()
        }

        for image in data:
            if 'photo' in image:
                if data[image]:
                    if not os.path.isfile("."+data[image]):
                        data[image] = None
                        continue

        # TODO: reformat
    
        return data

    @staticmethod
    def get_field_frontend_name(field):
        return fields_backend_to_frontend.get(field, field)

    @staticmethod
    def get_field_backend_name(field):
        return fields_frontend_to_backend.get(field, field)
