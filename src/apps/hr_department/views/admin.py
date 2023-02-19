from django.http import HttpResponse
from rest_framework.views import APIView
import json

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation
from apps.hr_department.serializers.serializers import UserSaveSerializer, \
    AdminDraftSerializer, AdminSaveSerializer
from apps.hr_department.serializers.utils.status import calculate_status, calculate_check_is_server_model
from apps.hr_department.views.decorators import add_user_id, add_owner_id, handler_all_decorator
from apps.hr_department.views.sends import not_valid_data, not_found, send_data, success_save
from apps.hr_department.views.utils import delete_drafts, delete_server_saves, get_serializer


class SearchHandler(APIView):
    @staticmethod
    def get(request):
        full_name = request.GET.get('full_name')
        server_employee_information = ServerEmployeeInformation.objects.filter(full_name__icontains=full_name)
        serializer = UserSaveSerializer(server_employee_information, many=True)

        reformatted_data = []
        for item in serializer.data:
            reformatted_data.append({key: value for key, value in item.items()})

        reformatted_data = json.dumps(reformatted_data)

        return HttpResponse(reformatted_data, content_type='application/json')


class AdminDraftHandler(APIView):
    @staticmethod
    @add_user_id
    @add_owner_id
    def post(request, user_id, owner_id):
        serializer = get_serializer(AdminDraftSerializer, DraftEmployeeInformation, request.clone_data, user_id=user_id,
                                    owner_id=owner_id)

        if not serializer.is_valid():
            return not_valid_data(request, serializer.errors)

        delete_drafts(user_id, owner_id)
        serializer.save()

        return HttpResponse(status=201)

    @staticmethod
    @handler_all_decorator(DraftEmployeeInformation, AdminDraftSerializer)
    @add_user_id
    @add_owner_id
    def get(request, user_id, owner_id):
        try:
            model = DraftEmployeeInformation.objects.get(user_id=user_id,
                                                         owner_id=owner_id)
        except DraftEmployeeInformation.DoesNotExist:
            return not_found(request)

        serializer = AdminDraftSerializer(model)

        return send_data(request, serializer.data)


class AdminSaveHandler(APIView):
    @staticmethod
    @add_user_id
    def post(request, user_id):
        serializer = get_serializer(AdminSaveSerializer, ServerEmployeeInformation, request.clone_data, user_id=user_id)

        if not serializer.is_valid():
            return not_valid_data(request, serializer.errors)

        is_editable = serializer.validated_data.get('is_editable', False)
        is_checked = serializer.validated_data.get('is_checked', False)
        data = {
            'is_editable': is_editable,
            'is_checked': is_checked,
            'user_id': user_id
        }
        status = calculate_check_is_server_model(data)
        serializer.validated_data['status'] = status
        serializer.save()

        return success_save(request)

    @staticmethod
    @handler_all_decorator(ServerEmployeeInformation, AdminSaveSerializer)
    @add_user_id
    def get(request, user_id):
        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return not_found(request)

        serializer = AdminSaveSerializer(model)

        return send_data(request, serializer.data)
