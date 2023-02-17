from django.db import models

genders = (
    ("male", "Муж"),
    ("female", "Жен")
)


class Education(models.Model):
    education_type = models.TextField(default=None, null=True, blank=True)
    educational_institution_name = models.TextField(default=None, null=True, blank=True)
    speciality = models.TextField(default=None, null=True, blank=True)
    qualification = models.TextField(default=None, null=True, blank=True)
    series_and_number = models.TextField(default=None, null=True, blank=True)
    date_of_issue = models.DateField(default=None, null=True)
    photo = models.ImageField(default="default.jpeg", null=True)
    language_proficiency = models.TextField(default=None, null=True, blank=True)
    date_range_of_education = models.DateField(default=None, null=True)


class Children(models.Model):
    full_name = models.TextField(default=None, null=True, blank=True)
    date_of_birthday = models.DateField(default=None, null=True)
    relation_degree = models.TextField(default=None, null=True, blank=True)


class FormField(models.Model):


    im_foreigner = models.BooleanField(default=False, null=True)
    full_name = models.TextField(default=None, null=True, blank=True)
    date_of_birthday = models.DateField(default=None, null=True)
    citizenship = models.TextField(default=None, null=True, blank=True)
    place_of_birthday = models.TextField(default=None, null=True, blank=True)
    email = models.TextField(default=None, null=True, blank=True)
    phone_number = models.TextField(default=None, null=True, blank=True)
    addresses_address_outside_russia = models.TextField(default=None, null=True, blank=True)
    addresses_address_for_information = models.TextField(default=None, null=True, blank=True)
    married_status_relation_degree = models.TextField(default=None, null=True, blank=True)
    married_status_full_name = models.TextField(default=None, null=True, blank=True)
    married_status_date_of_birthday = models.DateField(default=None, null=True)
    status_of_the_insured_person_status = models.TextField(default=None, null=True, blank=True)

    gender = models.TextField(choices=genders, default=None, null=True, blank=True)

    passport_series_and_number = models.TextField(default=None, null=True, blank=True)
    passport_issued_by = models.TextField(default=None, null=True, blank=True)
    passport_date_of_issue = models.DateField(default=None, null=True)
    passport_division_code = models.TextField(default=None, null=True, blank=True)
    passport_valid_until = models.DateField(default=None, null=True)
    passport_registered_address = models.TextField(default=None, null=True, blank=True)
    passport_registration_date = models.DateField(default=None, null=True)
    passport_reversal_photo = models.ImageField(default="default.jpeg", null=True)
    passport_registration_photo = models.ImageField(default=None, null=True)

    # many to many
    education = models.ManyToManyField(Education, default=[])

    military_document_relation_to_military_duty = models.TextField(default=None, null=True)
    military_document_rank = models.TextField(default=None, null=True)
    military_document_composition = models.TextField(default=None, null=True)
    military_document_stock_category = models.TextField(default=None, null=True)
    military_document_vus = models.TextField(default=None, null=True)
    military_document_fitness = models.TextField(default=None, null=True)
    military_document_commissariat = models.TextField(default=None, null=True)
    military_document_relation_to_military_registration = models.TextField(default=None, null=True)
    military_document_photo = models.ImageField(default="default.jpeg", null=True)

    # many to many
    children = models.ManyToManyField(Children, default=[])

    snils_number = models.TextField(default=None, null=True, blank=True)
    snils_photo = models.ImageField(default="default.jpeg", null=True)
    inn_number = models.TextField(default=None, null=True, blank=True)
    inn_photo = models.ImageField(default="default.jpeg", null=True)
    work_permit_series_and_number = models.TextField(default=None, null=True, blank=True)
    work_permit_date_of_issue = models.DateField(default=None, null=True)
    work_permit_valid_until = models.DateField(default=None, null=True)
    work_permit_issued_by = models.TextField(default=None, null=True, blank=True)
    work_permit_photo = models.ImageField(default="default.jpeg", null=True)
    residence_series_and_number = models.TextField(default=None, null=True, blank=True)
    residence_date_of_issue = models.DateField(default=None, null=True)
    residence_valid_until = models.DateField(default=None, null=True)
    residence_issued_by = models.TextField(default=None, null=True, blank=True)
    residence_photo = models.ImageField(default="default.jpeg", null=True)
    patent_series_and_number = models.TextField(default=None, null=True, blank=True)
    patent_date_of_issue = models.DateField(default=None, null=True)
    patent_valid_until = models.DateField(default=None, null=True)
    patent_issued_by = models.TextField(default=None, null=True, blank=True)
    patent_photo = models.ImageField(default="default.jpeg", null=True)
    temporary_residence_permit_series_and_number = models.TextField(default=None, null=True, blank=True)
    temporary_residence_permit_date_of_issue = models.DateField(default=None, null=True)
    temporary_residence_permit_valid_until = models.DateField(default=None, null=True)
    temporary_residence_permit_issued_by = models.TextField(default=None, null=True, blank=True)
    temporary_residence_permit_photo = models.ImageField(default="default.jpeg", null=True)
    migration_card_photo = models.ImageField(default="default.jpeg", null=True)
    notice_of_registration_in_russia_photo = models.ImageField(default="default.jpeg", null=True)

    wage_salary = models.TextField(default=None, null=True, blank=True)
    wage_di_award = models.TextField(default=None, null=True, blank=True)
    wage_monthly_mbo_award = models.TextField(default=None, null=True, blank=True)
    wage_mbo_award_quarter = models.TextField(default=None, null=True, blank=True)
    wage_quarterly_option = models.TextField(default=None, null=True, blank=True)
    wage_yearly_option = models.TextField(default=None, null=True, blank=True)
    wage_quasi_option = models.TextField(default=None, null=True, blank=True)

    vaccination_first_date = models.DateField(default=None, null=True)
    vaccination_second_date = models.DateField(default=None, null=True)

    is_checked = models.BooleanField(default=None, null=True)
    is_editable = models.BooleanField(default=None, null=True)

    status = models.TextField(default=None, null=True, blank=True)
    department = models.TextField(default=None, null=True, blank=True)
    supervisor = models.TextField(default=None, null=True, blank=True)

    @property
    def education_indexing(self):
        return [education_item for education_item in self.education.all()]

    @property
    def childrens_indexing(self):
        return [children_item for children_item in self.children.all()]

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
