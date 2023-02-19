from rest_framework.views import APIView

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftSerializer, \
    UserSaveSerializer
from apps.hr_department.views.decorators import add_user_id, handler_all_decorator
from apps.hr_department.views.sends import not_valid_data, success_save, not_found, \
    not_permission_save, send_data
from apps.hr_department.views.utils import delete_drafts, delete_server_saves, user_is_editable, \
    get_serializer



class UserDraftHandler(APIView):
    @staticmethod
    @add_user_id
    def post(request, user_id):
        request.clone_data['owner_id'] = request.clone_data['user_id']

        serializer = get_serializer(UserDraftSerializer, DraftEmployeeInformation, request.clone_data, user_id=user_id, owner_id=user_id)

        if not serializer.is_valid():
            return not_valid_data(request, serializer.errors)

        delete_drafts(user_id, user_id)
        serializer.save()

        return success_save(request)

    @staticmethod
    @handler_all_decorator(DraftEmployeeInformation, UserDraftSerializer)
    @add_user_id
    def get(request, user_id):
        try:
            model = DraftEmployeeInformation.objects.get(user_id=user_id,
                                                         owner_id=user_id)
        except DraftEmployeeInformation.DoesNotExist:
            return not_found(request)

        serializer = UserDraftSerializer(model)

        return send_data(request, serializer.data)


class UserSaveHandler(APIView):
    @staticmethod
    @add_user_id
    def post(request, user_id):
        request.clone_data['owner_id'] = request.clone_data['user_id']

        serializer = get_serializer(UserSaveSerializer, ServerEmployeeInformation, request.clone_data, user_id=user_id)

        if not serializer.is_valid():
            return not_valid_data(request, serializer.errors)

        if not user_is_editable(user_id):
            return not_permission_save(request)

        delete_drafts(user_id, user_id)

        serializer.validated_data['is_editable'] = False
        serializer.validated_data['is_checked'] = False
        serializer.validated_data['status'] = "user_sent"
        serializer.save()

        return success_save(request)

    @staticmethod
    @handler_all_decorator(ServerEmployeeInformation, UserSaveSerializer)
    @add_user_id
    def get(request, user_id):
        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return not_found(request)

        serializer = UserSaveSerializer(model)

        return send_data(request, serializer.data)
