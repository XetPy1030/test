from .models import ServerEmployeeInformation
from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
from django_elasticsearch_dsl.registries import registry

serversearchemployeeinformation = Index('serversearchemployeeinformation')
serversearchemployeeinformation.settings(
    number_of_shards=1,
    number_of_replicas=0
)


#
@serversearchemployeeinformation.doc_type
class ServerSearchEmployeeInformationDocument(Document):
    full_name = fields.TextField(
        attr='full_name',
        fields={
            'suggest': fields.CompletionField(),
        }
    )
    class Django:
        model = ServerEmployeeInformation
        fields = [
            'id',
            'user_id',
            'date_of_birthday',
        ]
