# elasticsearch-dsl-drf serializers for ServerSearchEmployeeInformationDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from apps.hr_department.documents import ServerSearchEmployeeInformationDocument


class ServerSearchEmployeeInformationDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ServerSearchEmployeeInformationDocument
        fields = (
            'id',
            'user_id',
            'full_name',
            'date_of_birthday',
        )