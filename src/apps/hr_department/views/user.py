from django.http import HttpResponse
from rest_framework.views import APIView
import json
from urllib3 import encode_multipart_formdata

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftSerializer, \
    UserSaveSerializer
from apps.hr_department.views.decorators import add_user_id
from apps.hr_department.views.errors import RequiredError, UserIsNotEditable
from apps.hr_department.views.utils import get_user_id, delete_drafts, delete_server_saves, user_is_editable


class UserDraftHandler(APIView):
    """
    Форма для заполнения черновика информации о сотруднике.
    Отправляется фронтендом.
    Сериализуется в модель DraftEmployeeInformation.
    И сохраняется в БД если валидация прошла успешно.
    Нужно для того, чтобы сотрудник мог сохранить свою форму и вернуться к ней позже.
    owner_id - id сотрудника, который заполняет форму.

    При создании черновика, owner_id и user_id должны быть одинаковыми.
    """

    @staticmethod
    @add_user_id
    def post(request, user_id):
        if not user_id:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        request.clone_data['owner_id'] = request.clone_data['user_id']

        serializer = UserDraftSerializer(data=request.clone_data)

        if not serializer.is_valid():
            return HttpResponse({'error': 'data in request not valid', 'errors': serializer.errors}, status=400)

        delete_drafts(user_id)
        serializer.save()

        return HttpResponse(status=201)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        Получает сам создатель.
        """
        if 'all' in request.GET:
            if request.GET.get('all') != 'true':
                return HttpResponse({'error': 'all must be true'}, status=401)
            models = DraftEmployeeInformation.objects.all()
            serializer = UserDraftSerializer(models, many=True)
            json_data = serializer.data
            json_data = json.dumps(json_data)
            return HttpResponse(json_data, content_type='application/json')

        try:
            user_id = get_user_id(request_data=None, request_get_data=request.GET, request_headers=request.headers)
        except RequiredError:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        try:
            model = DraftEmployeeInformation.objects.get(user_id=user_id,
                                                         owner_id=user_id)
        except DraftEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserDraftSerializer(model)

        json_data = serializer.data
        json_data = json.dumps(json_data)
        return HttpResponse(json_data, content_type='application/json')


class UserSaveHandler(APIView):
    """
    Сохраняет форму сотрудника в БД.
    И удаляет черновик из БД.
    """

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

        delete_drafts(user_id)
        delete_server_saves(user_id)

        serializer.validated_data['is_editable'] = False
        serializer.save()

        return HttpResponse(status=201)

    def get(self, request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        if 'all' in request.GET:
            if request.GET.get('all') != 'true':
                return HttpResponse({'error': 'all must be true'}, status=401)
            models = DraftEmployeeInformation.objects.all()
            serializer = UserDraftSerializer(models, many=True)
            json_data = serializer.data
            json_data = json.dumps(json_data)
            return HttpResponse(json_data, content_type='application/json')

        try:
            user_id = get_user_id(request_data=None, request_get_data=request.GET, request_headers=request.headers)
        except RequiredError:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserSaveSerializer(model)

        json_data = serializer.data

        type_of_send = 'json'
        return self.send_data(json_data, type_of_send)

    @staticmethod
    def send_data(json_data, type_of_send):
        if type_of_send == 'json':
            json_data = json.dumps(json_data)
            return HttpResponse(json_data, content_type='application/json')
        elif type_of_send == 'multipart':
            body, header = encode_multipart_formdata(json_data[0])
            return HttpResponse(body, content_type=header)
        else:
            return HttpResponse(status=500)

    @staticmethod
    def clean_none_values(data):
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
