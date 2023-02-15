from elasticsearch_dsl import analyzer, token_filter

from apps.hr_department.models import ServerEmployeeInformation
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

edge_ngram_completion_filter = token_filter(
    'edge_ngram_completion_filter',
    type="edge_ngram",
    min_gram=1,
    max_gram=20
)

edge_ngram_completion = analyzer(
    "edge_ngram_completion",
    tokenizer="standard",
    filter=["lowercase", edge_ngram_completion_filter]
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


#
@serversearchemployeeinformation.doc_type
class ServerSearchEmployeeInformationDocument(Document):
    id = fields.IntegerField(attr='id')
    full_name = fields.TextField(
        attr='full_name',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
            'edge_ngram_completion': fields.TextField(analyzer=edge_ngram_completion),
        }
    )

    class Django:
        model = ServerEmployeeInformation
        fields = [
            'user_id',
            'date_of_birthday',
            'email',
            'phone_number',
            'passport_series_and_number',
            'snils_number',
            'inn_number',
        ]
