from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftEmployeeInformationSerializer, \
    UserSaveEmployeeInformationSerializer


class UserDraftEmployeeHandler(APIView):
    """
    Форма для заполнения черновика информации о сотруднике.
    Отправляется фронтендом.
    Сериализуется в модель UserDraftEmployeeInformation.
    И сохраняется в БД если валидация прошла успешно.
    Нужно для того, чтобы сотрудник мог сохранить свою форму и вернуться к ней позже.
    owner_id - id сотрудника, который заполняет форму.

    При создании черновика, owner_id и user_id должны быть одинаковыми.
    """

    @staticmethod
    def post(request):
        serializer = UserDraftEmployeeInformationSerializer(data={key: value for key, value in request.data.items()})
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            models = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)
            serializer.save()
            return HttpResponse(status=201)
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


class UserSaveEmployeeDraftHandler(APIView):
    """
    Сохраняет форму сотрудника в БД.
    И удаляет черновик из БД.
    """

    @staticmethod
    def post(request):
        serializer = UserSaveEmployeeInformationSerializer(data={key: value for key, value in request.data.items()})
        # TODO: edit the object in DB EmployeeInformation
        if serializer.is_valid():
            serializer.save()

            user_id = serializer.validated_data['user_id']
            DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id).delete()

            return HttpResponse(status=201)
        return HttpResponse(status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        model = ServerEmployeeInformation.objects.all()[0]  # TODO: get the object by id from request
        serializer = UserSaveEmployeeInformationSerializer(model)
        return HttpResponse(serializer.data)

