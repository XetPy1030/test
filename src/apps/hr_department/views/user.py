from django.http import HttpResponse
from rest_framework.views import APIView
import json

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftSerializer, \
    UserSaveSerializer
from apps.hr_department.views.decorators import add_user_id, handler_all_decorator
from apps.hr_department.views.errors import RequiredError
from apps.hr_department.views.utils import get_user_id, delete_drafts, delete_server_saves, user_is_editable, send_data


class UserDraftHandler(APIView):
    @staticmethod
    @add_user_id
    def post(request, user_id):
        if not user_id:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        request.clone_data['owner_id'] = request.clone_data['user_id']

        serializer = UserDraftSerializer(data=request.clone_data)

        if not serializer.is_valid():
            return HttpResponse({'error': 'data in request not valid', 'errors': serializer.errors}, status=400)

        delete_drafts(user_id, user_id)
        serializer.save()

        return HttpResponse(status=201)

    @staticmethod
    @handler_all_decorator(DraftEmployeeInformation, UserDraftSerializer)
    @add_user_id
    def get(request, user_id):
        if not user_id:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        try:
            model = DraftEmployeeInformation.objects.get(user_id=user_id,
                                                         owner_id=user_id)
        except DraftEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserDraftSerializer(model)

        json_data = json.dumps(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


class UserSaveHandler(APIView):
    @staticmethod
    @add_user_id
    def post(request, user_id):
        if not user_id:
            return HttpResponse(json.dumps({'error': 'user_id not found in params request'}), status=401, content_type='application/json')

        request.clone_data['owner_id'] = request.clone_data['user_id']

        serializer = UserSaveSerializer(data=request.clone_data)

        if not serializer.is_valid():
            return HttpResponse(json.dumps({'error': 'data in request not valid', 'errors': serializer.errors}), status=400, content_type='application/json')

        if not user_is_editable(user_id):
            return HttpResponse(json.dumps({'error': 'user is not editable'}), status=400, content_type='application/json')

        delete_drafts(user_id, user_id)
        delete_server_saves(user_id)

        serializer.validated_data['is_editable'] = False
        serializer.save()

        return HttpResponse(status=201)

    @staticmethod
    @handler_all_decorator(DraftEmployeeInformation, UserDraftSerializer)
    @add_user_id
    def get(request, user_id):
        if not user_id:
            return HttpResponse(json.dumps({'error': 'user_id not found in params request'}), status=401, content_type='application/json')

        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserSaveSerializer(model)

        json_data = serializer.data

        type_of_send = 'json'
        return send_data(json_data, type_of_send)
