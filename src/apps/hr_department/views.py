from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.serializers import DraftEmployeeInformationSerializer
from apps.hr_department.tests import data_for_serializer
from apps.hr_department.utils.search_engine import search_by_full_name


# serializer = DraftEmployeeInformationSerializer(data=data_for_serializer)
# serializer.is_valid()
# serializer.save()


class FormDraftHandler(APIView):
    """
    Форма для заполнения информации о сотруднике.
    Отправляется фронтендом.
    Сериализуется в модель DraftEmployeeInformation.
    И сохраняется в БД если валидация прошла успешно.
    Нужно для того, чтобы сотрудник мог сохранить свою форму и вернуться к ней позже.
    """

    @staticmethod
    def post(request):
        serializer = DraftEmployeeInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

    @staticmethod
    def get(request):
        """
        Возвращает список всех полей модели DraftEmployeeInformation в виде json.
        """
        model = DraftEmployeeInformation.objects.all()[0]  # TODO: get the object by id from request
        serializer = DraftEmployeeInformationSerializer(model)
        return HttpResponse(serializer.data)


class SearchHandler(APIView):
    """
    Возвращает список сотрудников по полному имени.
    """

    @staticmethod
    def get(request):
        full_name = request.GET.get('full_name')
        server_employee_information = search_by_full_name(full_name)
        serializer = DraftEmployeeInformationSerializer(server_employee_information, many=True)
        return HttpResponse(serializer.data)
