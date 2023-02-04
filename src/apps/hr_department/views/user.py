from django.http import HttpResponse
from rest_framework.views import APIView
import json
from urllib3 import encode_multipart_formdata

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftSerializer, \
    UserSaveSerializer


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
    def post(request):
        clone = request.data.copy()

        if 'user_id' not in clone and 'user_id' not in request.GET:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        user_id = clone.get('user_id', request.GET.get('user_id'))
        clone['user_id'] = user_id
        clone['owner_id'] = clone['user_id']

        serializer = UserDraftSerializer(data=clone)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']

            # Удаляем старый черновик, если он есть.
            models = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)
            if models.exists():
                models.delete()

            # Сохраняем/создаем черновик.
            serializer.save()

            json_data = serializer.data
            json_data = json.dumps(json_data)
            return HttpResponse(json_data)

        return HttpResponse({'error': 'data in request not valid', 'errors': serializer.errors}, status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        Получает сам создатель.
        """
        if 'user_id' not in request.GET:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        user_id = request.GET.get('user_id')

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
    def post(request):
        clone = request.data.copy()

        if 'user_id' not in clone and 'user_id' not in request.GET:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        user_id = clone.get('user_id', request.GET.get('user_id'))
        clone['user_id'] = user_id

        serializer = UserSaveSerializer(data=clone)
        if serializer.is_valid():
            try:
                user = ServerEmployeeInformation.objects.get(user_id=user_id)
                if not user.is_editable and False:
                    return HttpResponse({'error': 'user is not editable'}, status=403)
            except ServerEmployeeInformation.DoesNotExist:
                pass

            users = ServerEmployeeInformation.objects.filter(user_id=user_id)
            drafts = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)
            if drafts.exists():
                drafts.delete()
            if users.exists():
                users.delete()

            serializer.validated_data['is_editable'] = False
            serializer.save()

            return HttpResponse(status=201)

        return HttpResponse(json.dumps({'error': 'data in request not valid', 'errors': serializer.errors}), status=400, content_type='application/json')

    def get(self, request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        if 'user_id' not in request.GET:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        user_id = request.GET.get('user_id')

        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserSaveSerializer(model)

        json_data = serializer.data
        self.clean_none_values(json_data)

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
