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
    # children
    # education
]

fields_backend = [
    'im_foreigner',  # boolean
    'full_name',  # string
    'date_of_birthday',  # date (YYYY-MM-DD)
    'citizenship',  # string
    'place_of_birthday',  # string
    'email',  # string (string@string.string)
    'phone_number',  # string (+7 (XXX)-XXX-XX-XX)
    'address_outside_russia',  # string
    'address_for_information',  # string
    'married_status_relation_degree',  # string
    'married_status_full_name',  # string
    'married_status_date_of_birthday',  # date (YYYY-MM-DD)
    'status_of_the_insured_person_status',  # string
    'gender',  # string (male/female)
    'passport_series_and_number',  # string (XX XX XXXXXX)
    'passport_issued_by',  # string
    'passport_date_of_issue,'  # date (YYYY-MM-DD)
    'passport_division_code',  # string (XXX-XXX)
    'passport_valid_until',  # date (YYYY-MM-DD)
    'passport_registration_date',  # date (YYYY-MM-DD)
    'passport_registered_address',  # string
    'passport_reversal_photo',  # file
    'passport_registration_photo',  # file
    'military_document_relation_to_military_duty',  # string
    'military_document_rank',  # string
    'military_document_composition',  # string
    'military_document_stock_category',  # string
    'military_document_vus',  # string
    'military_document_fitness',  # string
    'military_document_commissariat',  # string
    'military_document_relation_to_military_registration',  # string
    'military_document_photo',  # file
    'snils_number',  # string (XXX-XXX-XXX XX)
    'snils_photo',  # file
    'inn_number',  # string (XXX XXX XXX XXX)
    'inn_photo',  # file
    'work_permit_series_and_number',  # string
    'work_permit_date_of_issue',  # date (YYYY-MM-DD)
    'work_permit_valid_until',  # date (YYYY-MM-DD)
    'work_permit_issued_by',  # string
    'work_permit_photo',  # file
    'residence_series_and_number',  # string
    'residence_date_of_issue',  # date (YYYY-MM-DD)
    'residence_valid_until',  # date (YYYY-MM-DD)
    'residence_issued_by',  # string
    'residence_photo',  # file
    'patent_series_and_number',  # string
    'patent_date_of_issue',  # date (YYYY-MM-DD)
    'patent_valid_until',  # date (YYYY-MM-DD)
    'patent_issued_by',  # string
    'patent_photo',  # file
    'temporary_residence_permit_series_and_number',  # string
    'temporary_residence_permit_date_of_issue',  # date (YYYY-MM-DD)
    'temporary_residence_permit_valid_until',  # date (YYYY-MM-DD)
    'temporary_residence_permit_issued_by',  # string
    'temporary_residence_permit_photo',  # file
    'migration_card_photo',  # file
    'notice_of_registration_in_russia_photo',  # file
]

fields_frontend_to_backend = {
    key: value for key, value in zip(fields_frontend, fields_backend)
}

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
                'frontend_name': 'education_education_type',
            },
            {
                'backend_name': 'educational_institution_name',
                'frontend_name': 'education_educational_institution_name',
            },
            {
                'backend_name': 'speciality',
                'frontend_name': 'education_speciality',
            },
            {
                'backend_name': 'qualification',
                'frontend_name': 'education_qualification',
            },
            {
                'backend_name': 'series_and_number',
                'frontend_name': 'education_series_and_number',
            },
            {
                'backend_name': 'date_of_issue',
                'frontend_name': 'education_date_of_issue',
            },
            {
                'backend_name': 'date_range_of_education',
                'frontend_name': 'education_date_range_of_education',
            },
            {
                'backend_name': 'language_proficiency',
                'frontend_name': 'education_language_proficiency',
            },
            {
                'backend_name': 'photo',
                'frontend_name': 'education_photo',
            }
        ]
    },
    {
        'backend_name': 'childrens',
        'frontend_fields': [
            {
                'backend_name': 'full_name',
                'frontend_name': 'childrens_full_name',
            },
            {
                'backend_name': 'date_of_birthday',
                'frontend_name': 'childrens_date_of_birthday',
            },
            {
                'backend_name': 'relation_degree',
                'frontend_name': 'childrens_relation_degree',
            }
        ]
    }
]
