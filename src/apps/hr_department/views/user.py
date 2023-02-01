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
        user_id = request.GET.get('user_id')

        model = DraftEmployeeInformation.objects.filter(user_id=user_id,
                                                        owner_id=user_id)  # TODO: get the object by id from request

        if not model.exists():
            return HttpResponse(status=404)

        serializer = UserDraftSerializer(model, many=True)

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

        if 'user_id' not in clone:
            return HttpResponse({'error': 'user_id not found in params request'}, status=401)

        clone['owner_id'] = clone['user_id']

        serializer = UserSaveSerializer(data=clone)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']

            draft = DraftEmployeeInformation.objects.filter(user_id=user_id)
            user = ServerEmployeeInformation.objects.filter(user_id=user_id)
            if draft.exists():
                draft.delete()
            if user.exists():
                if not user.is_editable:
                    return HttpResponse({'error': 'user is not editable'}, status=403)
                user.delete()

            serializer.validated_data['is_editable'] = False
            serializer.save()

            return HttpResponse(status=201)

        return HttpResponse({'error': 'data in request not valid', 'errors': serializer.errors}, status=400)

    def get(self, request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        user_id = request.GET.get('user_id')
        model = ServerEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)  # TODO: get the object by id from request

        if not model.exists():
            return HttpResponse(status=404)

        serializer = UserSaveSerializer(model, many=True)

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
        for i in range(len(data)):
            for key in list(data[i].keys()):
                if data[i][key] is None:
                    del data[i][key]
