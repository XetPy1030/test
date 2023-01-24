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
    id = fields.IntegerField(attr='id')
    full_name = fields.TextField(
        attr='full_name',
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )

    location = fields.GeoPointField(attr='location')

    class Django:
        model = ServerEmployeeInformation
        fields = [
            'user_id',
            'date_of_birthday',
        ]
