from django.db import models

genders = (
    ("male", "Муж"),
    ("female", "Жен")
)


class FormField(models.Model):
    im_foreigner = models.BooleanField(default=None, null=True)
    full_name = models.TextField(default=None, null=True)
    date_of_birthday = models.DateField(default=None, null=True)
    citizenship = models.TextField(default=None, null=True)
    place_of_birthday = models.TextField(default=None, null=True)
    email = models.TextField(default=None, null=True)
    phone_number = models.TextField(default=None, null=True)
    address_outside_russia = models.TextField(default=None, null=True)
    address_for_information = models.TextField(default=None, null=True)
    married_status_relation_degree = models.TextField(default=None, null=True)
    married_status_full_name = models.TextField(default=None, null=True)
    married_status_date_of_birthday = models.DateField(default=None, null=True)
    status_of_the_insured_person_status = models.TextField(default=None, null=True)

    gender = models.TextField(choices=genders, default=None, null=True)

    passport_series_and_number = models.TextField(default=None, null=True)
    passport_issued_by = models.TextField(default=None, null=True)
    passport_date_of_issue = models.DateField(default=None, null=True)
    passport_division_code = models.TextField(default=None, null=True)
    passport_valid_until = models.DateField(default=None, null=True)
    passport_registered_address = models.TextField(default=None, null=True)
    passport_registration_date = models.DateField(default=None, null=True)
    passport_reversal_photo = models.ImageField(default=None, null=True)
    passport_registration_photo = models.ImageField(default=None, null=True)

    education_document_education_type = models.TextField(default=None, null=True)
    education_document_educational_institution_name = models.TextField(default=None, null=True)
    education_document_speciality = models.TextField(default=None, null=True)
    education_document_qualification = models.TextField(default=None, null=True)
    education_document_series_and_number = models.TextField(default=None, null=True)
    education_document_date_of_issue = models.DateField(default=None, null=True)
    education_document_date_range_of_education = models.TextField(default=None, null=True)
    education_document_language_proficiency = models.TextField(default=None, null=True)
    education_document_photo = models.TextField(default=None, null=True)

    military_document_relation_to_military_duty = models.TextField(default=None, null=True)
    military_document_rank = models.TextField(default=None, null=True)
    military_document_composition = models.TextField(default=None, null=True)
    military_document_stock_category = models.TextField(default=None, null=True)
    military_document_vus = models.TextField(default=None, null=True)
    military_document_fitness = models.BooleanField(default=None, null=True)
    military_document_commissariat = models.TextField(default=None, null=True)
    military_document_relation_to_military_registration = models.TextField(default=None, null=True)
    military_document_photo = models.ImageField(default=None, null=True)

    childrens_birth_certificates_full_name = models.TextField(default=None, null=True)
    childrens_birth_certificates_date_of_birthday = models.DateField(default=None, null=True)
    childrens_birth_certificates_relation_degree = models.TextField(default=None, null=True)
    snils_number = models.TextField(default=None, null=True)
    snils_photo = models.ImageField(default=None, null=True)
    inn_number = models.TextField(default=None, null=True)
    inn_photo = models.ImageField(default=None, null=True)
    work_permit_series_and_number = models.TextField(default=None, null=True)
    work_permit_date_of_issue = models.DateField(default=None, null=True)
    work_permit_valid_until = models.DateField(default=None, null=True)
    work_permit_issued_by = models.TextField(default=None, null=True)
    work_permit_photo = models.ImageField(default=None, null=True)
    residence_series_and_number = models.TextField(default=None, null=True)
    residence_date_of_issue = models.DateField(default=None, null=True)
    residence_valid_until = models.DateField(default=None, null=True)
    residence_issued_by = models.TextField(default=None, null=True)
    residence_photo = models.ImageField(default=None, null=True)
    patent_series_and_number = models.TextField(default=None, null=True)
    patent_date_of_issue = models.DateField(default=None, null=True)
    patent_valid_until = models.DateField(default=None, null=True)
    patent_issued_by = models.TextField(default=None, null=True)
    patent_photo = models.ImageField(default=None, null=True)
    temporary_residence_permit_series_and_number = models.TextField(default=None, null=True)
    temporary_residence_permit_date_of_issue = models.DateField(default=None, null=True)
    temporary_residence_permit_valid_until = models.DateField(default=None, null=True)
    temporary_residence_permit_issued_by = models.TextField(default=None, null=True)
    temporary_residence_permit_photo = models.ImageField(default=None, null=True)
    migration_card_photo = models.ImageField(default=None, null=True)
    notice_of_registration_in_russia_photo = models.ImageField(default=None, null=True)

    is_checked = models.BooleanField(default=None, null=True)


class Meta:
    abstract = True


class DraftEmployeeInformation(FormField):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.TextField()
    owner_id = models.TextField()


class ServerEmployeeInformation(FormField):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.TextField()
