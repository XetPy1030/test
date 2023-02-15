# elasticsearch-dsl-drf serializers for ServerSearchEmployeeInformationDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from apps.hr_department.documents import ServerSearchEmployeeInformationDocument
from apps.hr_department.documents.spreadSheet_search_document import SpreadSheetSearchEmployeeInformationDocument
from apps.hr_department.models import DraftEmployeeInformation
from apps.hr_department.utils import get_all_fields_for_document


class ServerSearchEmployeeInformationDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ServerSearchEmployeeInformationDocument
        fields = (
            'id',
            'user_id',
            'full_name',
            'date_of_birthday',
        )


class SpreadSheetSearchEmployeeInformationDocumentSerializer(DocumentSerializer):
    class Meta:
        document = SpreadSheetSearchEmployeeInformationDocument
        fields = tuple(get_all_fields_for_document(DraftEmployeeInformation))
