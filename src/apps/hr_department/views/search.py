from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.tests import data_for_serializer
from apps.hr_department.utils.search_engine import search_by_full_name
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from apps.hr_department.documents import ServerSearchEmployeeInformationDocument
from apps.hr_department.serializers.serializers import ServerSearchEmployeeInformationDocumentSerializer

from django_elasticsearch_dsl_drf.constants import (
    SUGGESTER_COMPLETION, LOOKUP_FILTER_GEO_DISTANCE

)

from django_elasticsearch_dsl_drf.filter_backends import (
    SuggesterFilterBackend
)


class ServerSearchEmployeeInformationDocumentViewSet(DocumentViewSet):
    document = ServerSearchEmployeeInformationDocument
    serializer_class = ServerSearchEmployeeInformationDocumentSerializer

    filter_backends = [
        SuggesterFilterBackend,
    ]

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

    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }
