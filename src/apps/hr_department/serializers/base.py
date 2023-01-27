import base64
from io import BytesIO

from PIL import Image
from rest_framework import serializers

from apps.hr_department.serializers.utils.fields import fields_frontend_to_backend, fields_backend_to_frontend
from apps.hr_department.serializers.utils.reformaters import reformat_frontend_fields


class BaseEmployeeInformationSerializer(serializers.ModelSerializer):
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
                    # with open("."+data[image], 'rb') as f:
                    #     img = f.read()
                    # data[image] = base64.b64encode(img).decode('utf-8')
                    img = Image.open("."+data[image])
                    buffered = BytesIO()
                    img.save(buffered, format="JPEG")
                    img_str = base64.b64encode(buffered.getvalue())
                    img_str = img_str.decode('utf-8')
                    # data[image] = f'<img src="data:image/jpeg;base64,{img_str}">'
                    data[image] = f'data:image/jpeg;base64,{img_str}'

        # TODO: reformat
    
        return data

    @staticmethod
    def get_field_frontend_name(field):
        return fields_backend_to_frontend.get(field, field)

    @staticmethod
    def get_field_backend_name(field):
        return fields_frontend_to_backend.get(field, field)
