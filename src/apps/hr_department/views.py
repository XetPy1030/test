from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.tests import data_for_serializer
from apps.hr_department.utils.search_engine import search_by_full_name
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from apps.hr_department.documents import DraftEmployeeInformationDocument
from apps.hr_department.serializers.serializers import DraftEmployeeInformationDocumentSerializer


from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)

from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)


# serializer = DraftEmployeeInformationSerializer(data=data_for_serializer)
# serializer.is_valid()
# serializer.save()

class DraftEmployeeInformationDocumentViewSet(DocumentViewSet):
    document = DraftEmployeeInformationDocument
    serializer_class = DraftEmployeeInformationDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
        DefaultOrderingFilterBackend,
        FacetedSearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'full_name',
        'inn_number',
        'passport_number',
        'snils_number',
    )
    # Define filtering fields
    filter_fields = {
        'full_name': 'full_name.raw',
        'inn_number': 'inn_number.raw',
        'passport_number': 'passport_number.raw',
        'snils_number': 'snils_number.raw',
    }

    suggester_fields = {
        'full_name_suggest': {
            'field': 'full_name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 10,
            },
        },
    }

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
