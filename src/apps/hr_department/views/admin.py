from django.http import HttpResponse
from rest_framework.views import APIView
import json

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation
from apps.hr_department.serializers.serializers import UserSaveSerializer, \
    UserDraftSerializer


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
    """
    Форма для заполнения черновика информации о сотруднике.
    Отправляется фронтендом.
    Сериализуется в модель AdminDraftEmployeeInformation.
    И сохраняется в БД если валидация прошла успешно.
    Нужно для того, чтобы сотрудник мог сохранить свою форму и вернуться к ней позже.
    owner_id - id сотрудника, который заполняет форму.
    user_id - id сотрудника, которого заполняют.

    При создании черновика, owner_id и user_id должны быть разными.
    """

    @staticmethod
    def post(request):
        # TODO: check for admin

        if 'user_id' not in request.data or 'owner_id' not in request.data:
            return HttpResponse({'error': 'user_id or owner_id not in request'}, status=400)

        serializer = UserDraftSerializer(data={key: value for key, value in request.data.items()})
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            owner_id = serializer.validated_data['owner_id']

            # Удаляем старый черновик, если он есть.
            models = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=owner_id)
            if models.exists():
                models.delete()

            # Сохраняем/создаем черновик.
            serializer.save()

            return HttpResponse(status=201)

        return HttpResponse({'error': 'data in request not valid', 'errors': serializer.errors}, status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        Получает сам создатель. Owner_id = user_id.
        """

        if 'user_id' not in request.data or 'owner_id' not in request.data:
            return HttpResponse({'error': 'user_id or owner_id not in request'}, status=400)

        owner_id = request.GET['owner_id']
        user_id = request.GET['user_id']

        try:
            model = DraftEmployeeInformation.objects.get(owner_id=owner_id, user_id=user_id)
        except DraftEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserDraftSerializer(model)

        data = serializer.data
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')


class AdminSaveHandler(APIView):
    """
    Сохраняет форму сотрудника в БД.
    И удаляет черновик из БД.
    """

    @staticmethod
    def post(request):
        if 'user_id' not in request.data or 'owner_id' not in request.data:
            return HttpResponse({'error': 'user_id or owner_id not in request'}, status=400)

        serializer = UserSaveSerializer(data={key: value for key, value in request.data.items()})
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            owner_id = serializer.validated_data['owner_id']

            # Удаляем старый черновик, если он есть.
            models = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=owner_id)
            if models.exists():
                models.delete()
            models = ServerEmployeeInformation.objects.filter(user_id=user_id)
            if models.exists():
                models.delete()

            serializer.save()

            return HttpResponse(status=201)

        return HttpResponse({'error': 'data in request not valid', 'errors': serializer.errors}, status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """

        if 'user_id' not in request.data or 'owner_id' not in request.data:
            return HttpResponse({'error': 'user_id or owner_id not in request'}, status=400)

        owner_id = request.GET['owner_id']
        user_id = request.GET['user_id']

        try:
            model = ServerEmployeeInformation.objects.get(user_id=user_id)
        except ServerEmployeeInformation.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserSaveSerializer(model)

        data = serializer.data
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
