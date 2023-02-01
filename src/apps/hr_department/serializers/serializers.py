from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.base import BaseSerializer


class UserDraftSerializer(BaseSerializer):
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


class UserSaveSerializer(BaseSerializer):
    class Meta:
        model = ServerEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]


class AdminDraftSerializer(BaseSerializer):
    class Meta:
        model = DraftEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]


class AdminSaveSerializer(BaseSerializer):
    class Meta:
        model = ServerEmployeeInformation
        fields = '__all__'
        validators = [
            # NotMeValidator()
        ]
