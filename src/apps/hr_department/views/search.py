from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from apps.hr_department.documents.spreadSheet_search_document import SpreadSheetSearchEmployeeInformationDocument
from apps.hr_department.serializers.document_serializers import SpreadSheetSearchEmployeeInformationDocumentSerializer

from apps.hr_department.documents.admin_search_document import ServerSearchEmployeeInformationDocument
from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.serializers.document_serializers import ServerSearchEmployeeInformationDocumentSerializer
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination, QueryFriendlyPageNumberPagination

from django_elasticsearch_dsl_drf.constants import (
    SUGGESTER_COMPLETION, LOOKUP_FILTER_GEO_DISTANCE, LOOKUP_FILTER_RANGE, LOOKUP_QUERY_IN, LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE, LOOKUP_QUERY_LT, LOOKUP_QUERY_LTE, FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
    FUNCTIONAL_SUGGESTER_COMPLETION_MATCH, LOOKUP_QUERY_CONTAINS

)

from django_elasticsearch_dsl_drf.filter_backends import (
    SuggesterFilterBackend, SearchFilterBackend, FunctionalSuggesterFilterBackend, FilteringFilterBackend,
    OrderingFilterBackend, DefaultOrderingFilterBackend, IdsFilterBackend
)

from apps.hr_department.utils import get_all_fields_for_document


class ServerSearchEmployeeInformationDocumentViewSet(DocumentViewSet):
    document = ServerSearchEmployeeInformationDocument
    serializer_class = ServerSearchEmployeeInformationDocumentSerializer

    filter_backends = [
        SearchFilterBackend,
        SuggesterFilterBackend,
        FunctionalSuggesterFilterBackend,
    ]

    search_fields = [
        'id',
    ]

    filtering_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
    }

    functional_suggester_fields = {
        'full_name_suggest': {
            'field': 'full_name.raw',
            'suggesters': [
                FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
            ],
            'default_suggester': FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
            'options': {
                'size': 10,
            },
        },
        'full_name_suggest_match': {
            'field': 'full_name.edge_ngram_completion',
            'suggesters': [FUNCTIONAL_SUGGESTER_COMPLETION_MATCH],
            'default_suggester': FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
            'options': {
                'size': 10,
            },
        },
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

    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }


class SpreadSheetSearchEmployeeInformationDocumentViewSet(DocumentViewSet):
    document = SpreadSheetSearchEmployeeInformationDocument

    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    pagination_class = QueryFriendlyPageNumberPagination

    # search_fields all
    search_fields = tuple(get_all_fields_for_document(DraftEmployeeInformation) + ['id'])

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        # for all fields
        **{field: {
            'field': field,
            'lookups': [
                LOOKUP_QUERY_CONTAINS
            ]} for field in get_all_fields_for_document(DraftEmployeeInformation)
        },
    }

    # generate ordering_fields
    ordering_fields = {
        'id': 'id',
        **{field: field + ".raw" for field in get_all_fields_for_document(DraftEmployeeInformation)}
    }
    ordering = ('id',)
