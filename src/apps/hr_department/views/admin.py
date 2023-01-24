from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.serializers import ServerSearchEmployeeInformationDocumentSerializer
from apps.hr_department.serializers.serializers import DraftEmployeeInformationSerializer
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
