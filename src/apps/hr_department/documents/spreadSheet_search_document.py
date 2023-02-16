from elasticsearch_dsl import analyzer, token_filter
from apps.hr_department.models import ServerEmployeeInformation
from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)

from apps.hr_department.utils import get_all_fields_for_document
from apps.hr_department.utils.get_all_fields import get_date_fields_for_document

# document for spreadSheet_search_document

spreadSheet_search_document = Index('spreadsheet_search_document')
spreadSheet_search_document.settings(
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


@spreadSheet_search_document.doc_type
class SpreadSheetSearchEmployeeInformationDocument(Document):
    id = fields.IntegerField(attr='id')

    date_fields, other_fields = get_date_fields_for_document(ServerEmployeeInformation)

    for field in date_fields:
        locals()[field] = fields.TextField(
            attr=field,
            analyzer="keyword",
        )

    # generate fields for all fields_list
    for field in other_fields:
        if field == 'user_id' or field == 'full_name':
            continue
        locals()[field] = fields.TextField(
            attr=field,
            analyzer=html_strip,
            fields={
                'raw': fields.TextField(analyzer='keyword')
            }
        )
    full_name = fields.TextField(
        attr="full_name",
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )

    class Django:
        model = ServerEmployeeInformation
        fields = [
            'user_id',
        ]