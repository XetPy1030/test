from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation
from apps.hr_department.serializers import ServerSearchEmployeeInformationDocumentSerializer
from apps.hr_department.serializers.serializers import DraftEmployeeInformationSerializer, \
    UserSaveEmployeeInformationSerializer, UserDraftEmployeeInformationSerializer
from apps.hr_department.utils.search_engine import search_by_full_name
from config.settings import MAX_LENGTH_FOR_SEARCH_USERS


class SearchHandler(APIView):
    """
    Возвращает список сотрудников по полному имени.
    Отправитель: Администратор.
    """

    @staticmethod
    def get(request):
        full_name = request.GET.get('full_name')
        # TODO: check for admin
        server_employee_information = search_by_full_name(full_name, max_length=MAX_LENGTH_FOR_SEARCH_USERS)
        serializer = DraftEmployeeInformationSerializer(server_employee_information, many=True)
        return HttpResponse(serializer.data)


class AdminDraftEmployeeHandler(APIView):
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

    def post(self, request):
        serializer = UserDraftEmployeeInformationSerializer(data={key: value for key, value in request.data.items()})
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
        print(serializer.errors)
        return HttpResponse(status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        Получает сам создатель. Owner_id = user_id.
        """

        model = DraftEmployeeInformation.objects.all()[0]  # TODO: get the object by id from request
        serializer = UserDraftEmployeeInformationSerializer(model)
        return HttpResponse(serializer.data)


class AdminSaveEmployeeDraftHandler(APIView):
    """
    Сохраняет форму сотрудника в БД.
    И удаляет черновик из БД.
    """
    @staticmethod
    def post(request):
        serializer = UserSaveEmployeeInformationSerializer(data={key: value for key, value in request.data.items()})
        if serializer.is_valid():
            serializer.save()

            return HttpResponse(status=201)
        return HttpResponse(status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        model = ServerEmployeeInformation.objects.all()[0]
        serializer = UserSaveEmployeeInformationSerializer(model)
        return HttpResponse(serializer.data)

