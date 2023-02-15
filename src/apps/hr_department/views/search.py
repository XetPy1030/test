from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from apps.hr_department.documents.admin_search_document import ServerSearchEmployeeInformationDocument
from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.serializers.document_serializers import ServerSearchEmployeeInformationDocumentSerializer

from django_elasticsearch_dsl_drf.constants import (
    SUGGESTER_COMPLETION, LOOKUP_FILTER_GEO_DISTANCE, LOOKUP_FILTER_RANGE, LOOKUP_QUERY_IN, LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE, LOOKUP_QUERY_LT, LOOKUP_QUERY_LTE, FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
    FUNCTIONAL_SUGGESTER_COMPLETION_MATCH, LOOKUP_FILTER_EXISTS

)

from django_elasticsearch_dsl_drf.filter_backends import (
    SuggesterFilterBackend, SearchFilterBackend, FunctionalSuggesterFilterBackend, FilteringFilterBackend,
    OrderingFilterBackend, DefaultOrderingFilterBackend
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


# viewSets for spreadSheet_search_document
from apps.hr_department.documents.spreadSheet_search_document import SpreadSheetSearchEmployeeInformationDocument
from apps.hr_department.serializers.document_serializers import SpreadSheetSearchEmployeeInformationDocumentSerializer


class SpreadSheetSearchEmployeeInformationDocumentViewSet(DocumentViewSet):
    document = SpreadSheetSearchEmployeeInformationDocument
    serializer_class = SpreadSheetSearchEmployeeInformationDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # search_fields all
    search_fields = get_all_fields_for_document(DraftEmployeeInformation) + ['id']

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
                LOOKUP_FILTER_EXISTS
            ]} for field in get_all_fields_for_document(DraftEmployeeInformation)
        },
    }

    # dsl drf ordering_fields all
    # get_all_fields_for_document(DraftEmployeeInformation) + ['id']

    # generate ordering_fields
    ordering_fields = {
        'id': 'id',
        **{field: field + ".raw" for field in get_all_fields_for_document(DraftEmployeeInformation)}
    }
    ordering = ('id',)
