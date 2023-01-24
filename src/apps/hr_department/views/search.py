from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.tests import data_for_serializer
from apps.hr_department.utils.search_engine import search_by_full_name
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from apps.hr_department.documents import ServerSearchEmployeeInformationDocument
from apps.hr_department.serializers.serializers import ServerSearchEmployeeInformationDocumentSerializer

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_EXCLUDE,
    LOOKUP_QUERY_ISNULL,
    LOOKUP_QUERY_STARTSWITH,
    LOOKUP_QUERY_IN, SUGGESTER_COMPLETION,

)

from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend, OrderingFilterBackend, CompoundSearchFilterBackend,
)


class ServerSearchEmployeeInformationDocumentViewSet(DocumentViewSet):
    document = ServerSearchEmployeeInformationDocument
    serializer_class = ServerSearchEmployeeInformationDocumentSerializer

    filtering_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = ("full_name",)

    filter_fields = {
        "id": {
            "field": "id",
            "lookups": [
                LOOKUP_QUERY_IN,
                ],
            },
        }

    suggester_fields = {
        "full_name_suggest": {
            "field": "full_name_suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
                ],
        }
    }
