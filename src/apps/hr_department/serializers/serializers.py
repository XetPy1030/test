from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.base import BaseEmployeeInformationSerializer
from apps.hr_department.documents import ServerSearchEmployeeInformationDocument
from apps.hr_department.validators.other_validators import NotMeValidator


class DraftEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = DraftEmployeeInformation
        fields = '__all__'
        validators = [
            # JwtTokenValidator(),
        ]


# elasticsearch-dsl-drf serializers for ServerSearchEmployeeInformationDocument
class ServerSearchEmployeeInformationDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ServerSearchEmployeeInformationDocument
        fields = (
            'id',
            'user_id',
            'full_name',
            'date_of_birthday',
        )

class UserDraftEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = DraftEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data['owner_id'] = data['user_id']
        return data


class UserSaveEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = ServerEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]
