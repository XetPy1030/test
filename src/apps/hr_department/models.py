from django.db import models

from config.env_variables import PICTURES_FOLDER

# Create your models here.

genders = (
    ("MALE", "Муж"),
    ("FEMALE", "Жен")
)


class FormField(models.Model):
    inn_photo = models.ImageField(upload_to=PICTURES_FOLDER)
    snils_photo = models.ImageField(upload_to=PICTURES_FOLDER)

    full_name = models.TextField(default=None, null=True)
    date_of_birthday = models.DateField(default=None, null=True)

    gender_gender = models.TextField(choices=genders, default=None, null=True)
    inn_number = models.TextField(default=None, null=True)
    snils_number = models.TextField(default=None, null=True)

    passport_series_and_number = models.IntegerField(default=None, null=True)
    passport_issued_by = models.TextField(default=None, null=True)
    passport_date_of_issue = models.DateField(default=None, null=True)
    passport_division_code = models.TextField(default=None, null=True)
    passport_registered_address = models.TextField(default=None, null=True)
    passport_photo1 = models.ImageField(default=None, null=True)
    passport_photo2 = models.ImageField(default=None, null=True)

    place_of_birthday = models.TextField(default=None, null=True)
    citizenship = models.TextField(default=None, null=True)
    address_of_residence = models.TextField(default=None, null=True)
    is_civil_servant = models.BooleanField(default=None, null=True)
    date_of_vaccination = models.DateField(default=None, null=True)
    education = models.TextField(default=None, null=True)


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



"""
im_foreigner__im_foreigner - bool - 11
full_name__full_name - str - 11
date_of_birthday__date - date - 11
citizenship__citizenship - str - 01
place_of_birthday__place - str - 11
email__email - str - 11
phone_number__phone_number - str - 11
addresses__address_outside_russia - str - 01
addresses__address_for_information - str - 01
married_status__relation_degree - str - 01
married_status__full_name - str - 01
married_status__date_of_birthday - date - 01
status_of_the_insured_person__status - str - 01
gender__gender - str - 10
passport__series_and_number - str - 11
passport__issued_by - str - 11
passport__date_of_issue - date - 11
passport__division_code - str - 11
passport__valid_until - date - 01
passport__registration_date - date - 10
passport__registered_address - str - 10
passport__reversal_photo - image - 11
passport__registration_photo - image - 10

НЕСКОЛЬКО
education_document__education_type - str - 11
education_document__educational_institution_name - str - 11
education_document__speciality - str - 11
education_document__qualification - str - 1
education_document__series_and_number - str - 1
education_document__date_of_issue - date - 1
education_document__date_range_of_education - str - 01
 -education_document__language_proficiency - str - 01
education_document__photo - str - 11

military_document__relation_to_military_duty - str - 10
military_document__rank - str - 10
military_document__composition - str - 10
military_document__stock_category - str - 10
military_document__vus - str - 10
military_document__fitness - bool - 10
military_document__commissariat - str - 10
military_document__relation_to_military_registration - str - 10
military_document__photo - image - 10

НЕСКОЛЬКО
childrens_birth_certificates__full_name - str - 10
childrens_birth_certificates__date_of_birthday - date - 10
childrens_birth_certificates__relation_degree - str - 10

snils__number - str - 11
snils__photo - image - 11
inn__number - str - 11
inn__photo - image - 11
work_permit__series_and_number - str - 01
work_permit__date_of_issue - date - 01
work_permit__valid_until - date - 01
work_permit__issued_by - str - 01
work_permit__photo - image - 01
residence__series_and_number - str - 01
residence__date_of_issue - date - 01
residence__valid_until - date - 01
residence__issued_by - str - 01
residence__photo - image - 01
patent__series_and_number - str - 01
patent__date_of_issue - date - 01
patent__valid_until - date - 01
patent__issued_by - str - 01
patent__photo - image - 01
temporary_residence_permit__series_and_number - str - 01
temporary_residence_permit__date_of_issue - date - 01
temporary_residence_permit__valid_until - date - 01
temporary_residence_permit__issued_by - str - 01
temporary_residence_permit__photo - image - 01
migration_card__photo - image - 01
notice_of_registration_in_russia__photo - image - 01

"""

