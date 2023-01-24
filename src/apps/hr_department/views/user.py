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

    def post(self, request):
        clone = request.data.copy()
        clone['owner_id'] = clone['user_id']
        serializer = UserDraftEmployeeInformationSerializer(data=clone)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']

            # Удаляем старый черновик, если он есть.
            models = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)
            if models.exists():
                models.delete()

            # Сохраняем/создаем черновик.
            serializer.save()

            return HttpResponse(status=201)

        return HttpResponse(serializer.errors, status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        Получает сам создатель.
        """
        user_id = request.GET.get('user_id')

        model = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)  # TODO: get the object by id from request

        if not model.exists():
            return HttpResponse(status=404)

        serializer = UserDraftEmployeeInformationSerializer(model)

        return HttpResponse(serializer.data, status=200)


class UserSaveEmployeeDraftHandler(APIView):
    """
    Сохраняет форму сотрудника в БД.
    И удаляет черновик из БД.
    """
    @staticmethod
    def post(request):
        clone = request.data.copy()
        clone['owner_id'] = clone['user_id']
        serializer = UserSaveEmployeeInformationSerializer(data=clone)
        # TODO: edit the object in DB EmployeeInformation
        if serializer.is_valid():
            serializer.save()

            user_id = serializer.validated_data['user_id']
            draft = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)
            if draft.exists():
                draft.delete()

            return HttpResponse(status=201)

        return HttpResponse(serializer.errors, status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        user_id = request.GET.get('user_id')
        model = ServerEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)  # TODO: get the object by id from request

        if not model.exists():
            return HttpResponse(status=404)

        serializer = UserSaveEmployeeInformationSerializer(model)

        return HttpResponse(serializer.data)
