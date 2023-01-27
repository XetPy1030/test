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

    class Django:
        model = ServerEmployeeInformation
        fields = [
            'im_foreigner',
            'user_id',
            'date_of_birthday',
            'citizenship',
            'place_of_birthday',
            'email',
            'phone_number',
            'passport_issued_by',
            'passport_series_and_number',
            'passport_date_of_issue',
            'passport_division_code',
            'passport_valid_until',
            'passport_registered_address',
            'passport_registration_date',
            'education_document_education_type',
            'education_document_educational_institution_name',
            'education_document_speciality',
            'education_document_qualification',
            'education_document_series_and_number',
            'education_document_date_of_issue',
            'education_document_date_range_of_education',
            'education_document_language_proficiency',
            'military_document_relation_to_military_duty',
            'military_document_rank',
            'military_document_composition',
            'military_document_stock_category',
            'military_document_vus',
            'military_document_fitness',
            'military_document_commissariat',
            'military_document_relation_to_military_registration',
            'childrens_birth_certificates_full_name',
            'childrens_birth_certificates_date_of_birthday',
            'childrens_birth_certificates_relation_degree',
            'snils_number',
            'inn_number',
            'work_permit_series_and_number',
            'work_permit_date_of_issue',
            'work_permit_valid_until',
            'work_permit_issued_by',
            'residence_series_and_number',
            'residence_date_of_issue',
            'residence_valid_until',
            'residence_issued_by',
            'patent_series_and_number',
            'patent_date_of_issue',
            'patent_valid_until',
            'patent_issued_by',
            'temporary_residence_permit_series_and_number',
            'temporary_residence_permit_date_of_issue',
            'temporary_residence_permit_valid_until',
            'temporary_residence_permit_issued_by',
            'is_checked',
        ]
