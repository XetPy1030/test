from rest_framework import serializers

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.base import BaseEmployeeInformationSerializer
from apps.hr_department.serializers.reformaters import reformat_frontend_fields
from apps.hr_department.serializers.token_refactor import jwt_token_refactor
from apps.hr_department.validators.other_validators import NotMeValidator


class DraftEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = DraftEmployeeInformation
        fields = '__all__'
        validators = [
            # JwtTokenValidator(),
        ]


class UserDraftEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = DraftEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]

    def to_internal_value(self, data):
        jwt_token_refactor(data)
        data['owner_id'] = data['user_id']

        return super().to_internal_value(data)


class UserSaveEmployeeInformationSerializer(BaseEmployeeInformationSerializer):
    class Meta:
        model = ServerEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]
