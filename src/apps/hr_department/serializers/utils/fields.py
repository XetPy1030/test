

fields_frontend = [
    'im_foreigner__im_foreigner',
    'full_name__full_name',
    'date_of_birthday__date',
    'citizenship__citizenship',
    'place_of_birthday__place',
    'email__email',
    'phone_number__phone_number',
    'addresses__address_outside_russia',
    'addresses__address_for_information',
    'married_status__relation_degree',
    'married_status__full_name',
    'married_status__date_of_birthday',
    'status_of_the_insured_person__status',
    'gender__gender',
    'passport__series_and_number',
    'passport__issued_by',
    'passport__date_of_issue',
    'passport__division_code',
    'passport__valid_until',
    'passport__registration_date',
    'passport__registered_address',
    'passport__reversal_photo',
    'passport__registration_photo',
    'military_document__relation_to_military_duty',
    'military_document__rank',
    'military_document__composition',
    'military_document__stock_category',
    'military_document__vus',
    'military_document__fitness',
    'military_document__commissariat',
    'military_document__relation_to_military_registration',
    'military_document__photo',
    'snils__number',
    'snils__photo',
    'inn__number',
    'inn__photo',
    'work_permit__series_and_number',
    'work_permit__date_of_issue',
    'work_permit__valid_until',
    'work_permit__issued_by',
    'work_permit__photo',
    'residence__series_and_number',
    'residence__date_of_issue',
    'residence__valid_until',
    'residence__issued_by',
    'residence__photo',
    'patent__series_and_number',
    'patent__date_of_issue',
    'patent__valid_until',
    'patent__issued_by',
    'patent__photo',
    'temporary_residence_permit__series_and_number',
    'temporary_residence_permit__date_of_issue',
    'temporary_residence_permit__valid_until',
    'temporary_residence_permit__issued_by',
    'temporary_residence_permit__photo',
    'migration_card__photo',
    'notice_of_registration_in_russia__photo',
]
fields_backend = [
    'im_foreigner',
    'full_name',
    'date_of_birthday',
    'citizenship',
    'place_of_birthday',
    'email',
    'phone_number',
    'address_outside_russia',
    'address_for_information',
    'married_status_relation_degree',
    'married_status_full_name',
    'married_status_date_of_birthday',
    'status_of_the_insured_person_status',
    'gender',
    'passport_series_and_number',
    'passport_issued_by',
    'passport_date_of_issue',
    'passport_division_code',
    'passport_valid_until',
    'passport_registration_date',
    'passport_registered_address',
    'passport_reversal_photo',
    'passport_registration_photo',
    'military_document_relation_to_military_duty',
    'military_document_rank',
    'military_document_composition',
    'military_document_stock_category',
    'military_document_vus',
    'military_document_fitness',
    'military_document_commissariat',
    'military_document_relation_to_military_registration',
    'military_document_photo',
    'snils_number',
    'snils_photo',
    'inn_number',
    'inn_photo',
    'work_permit_series_and_number',
    'work_permit_date_of_issue',
    'work_permit_valid_until',
    'work_permit_issued_by',
    'work_permit_photo',
    'residence_series_and_number',
    'residence_date_of_issue',
    'residence_valid_until',
    'residence_issued_by',
    'residence_photo',
    'patent_series_and_number',
    'patent_date_of_issue',
    'patent_valid_until',
    'patent_issued_by',
    'patent_photo',
    'temporary_residence_permit_series_and_number',
    'temporary_residence_permit_date_of_issue',
    'temporary_residence_permit_valid_until',
    'temporary_residence_permit_issued_by',
    'temporary_residence_permit_photo',
    'migration_card_photo',
    'notice_of_registration_in_russia_photo',
]

fields_frontend_to_backend = {
    key: value for key, value in zip(fields_frontend, fields_backend)
}

# using for and zip
fields_backend_to_frontend = {
    key: value for key, value in zip(fields_backend, fields_frontend)
}

date_fields = [
    'passport_registration_date',
    'date_of_birthday',
    'work_permit_date_of_issue',
    'married_status_date_of_birthday',
    'passport_date_of_issue',
    'patent_date_of_issue',
    'temporary_residence_permit_date_of_issue',
    'residence_date_of_issue',
    'education_document_date_range_of_education'
    'education_document_date_of_issue',
    'childrens_birth_certificates_date_of_birthday',
    'education_document_date_of_issue'
]

iter_fields = [
    {
        'backend_name': 'education',
        'frontend_fields': [
            {
                'backend_name': 'education_type',
                'frontend_name': 'education__education_type',
            },
            {
                'backend_name': 'educational_institution_name',
                'frontend_name': 'education__educational_institution_name',
            },
            {
                'backend_name': 'speciality',
                'frontend_name': 'education__speciality',
            },
            {
                'backend_name': 'qualification',
                'frontend_name': 'education__qualification',
            },
            {
                'backend_name': 'series_and_number',
                'frontend_name': 'education__series_and_number',
            },
            {
                'backend_name': 'date_of_issue',
                'frontend_name': 'education__date_of_issue',
            },
            {
                'backend_name': 'date_range_of_education',
                'frontend_name': 'education__date_range_of_education',
            },
            {
                'backend_name': 'language_proficiency',
                'frontend_name': 'education__language_proficiency',
            },
            {
                'backend_name': 'photo',
                'frontend_name': 'education__photo',
            }
        ]
    },
    {
        'backend_name': 'childrens',
        'frontend_fields': [
            {
                'backend_name': 'full_name',
                'frontend_name': 'children__full_name',
            },
            {
                'backend_name': 'date_of_birthday',
                'frontend_name': 'children__date_of_birthday',
            },
            {
                'backend_name': 'relation_degree',
                'frontend_name': 'children__relation_degree',
            }
        ]
    }
]
