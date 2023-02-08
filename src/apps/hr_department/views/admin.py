from django.http import HttpResponse
from rest_framework.views import APIView
import json

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation
from apps.hr_department.serializers.serializers import UserSaveSerializer, \
    UserDraftSerializer, AdminDraftSerializer, AdminSaveSerializer
from apps.hr_department.views.decorators import add_user_id, add_owner_id, handler_all_decorator
from apps.hr_department.views.utils import delete_drafts, delete_server_saves, send_data, get_serializer


class SearchHandler(APIView):
    """
    Возвращает список сотрудников по полному имени.
    Отправитель: Администратор.
    """

    @staticmethod
    def get(request):
        full_name = request.GET.get('full_name')
        # TODO: check for admin
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
        if not user_id:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)
        if not owner_id:
            return HttpResponse({'error': 'owner_id not found in params request'}, status=401)

        serializer = get_serializer(AdminDraftSerializer, DraftEmployeeInformation, request.clone_data, user_id=user_id, owner_id=owner_id)

        if not serializer.is_valid():
            return HttpResponse(json.dumps({'error': 'data in request not valid', 'errors': serializer.errors}), status=400)

        delete_drafts(user_id, owner_id)
        serializer.save()

        return HttpResponse(status=201)

    @staticmethod
    @handler_all_decorator(DraftEmployeeInformation, AdminDraftSerializer)
    @add_user_id
    @add_owner_id
    def get(request, user_id, owner_id):
        if not user_id:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)
        if not owner_id:
            return HttpResponse({'error': 'owner_id not found in params request'}, status=401)

        try:
            model = DraftEmployeeInformation.objects.get(user_id=user_id,
                                                         owner_id=owner_id)
        except DraftEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = AdminDraftSerializer(model)

        json_data = json.dumps(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


class AdminSaveHandler(APIView):
    @staticmethod
    @add_user_id
    def post(request, user_id):
        if not user_id:
            return HttpResponse(json.dumps({'error': 'user_id not found in params request'}), status=401, content_type='application/json')

        serializer = get_serializer(AdminSaveSerializer, ServerEmployeeInformation, request.clone_data, user_id=user_id)

        if not serializer.is_valid():
            return HttpResponse(json.dumps({'error': 'data in request not valid', 'errors': serializer.errors}), status=400, content_type='application/json')

        delete_server_saves(user_id)

        serializer.save()

        return HttpResponse(status=201)

    @staticmethod
    @handler_all_decorator(ServerEmployeeInformation, AdminSaveSerializer)
    @add_user_id
    def get(request, user_id):
        if not user_id:
            return HttpResponse(json.dumps({'error': 'user_id not found in params request'}), status=401, content_type='application/json')

        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = AdminSaveSerializer(model)

        json_data = serializer.data

        type_of_send = 'json'
        return send_data(json_data, type_of_send)
