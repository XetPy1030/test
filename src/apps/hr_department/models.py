from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from config.env_variables import PICTURES_FOLDER

# Create your models here.

genders = (
    ("MALE", "Муж"),
    ("FEMALE", "Жен")
)

# 6d88094b-4b8c-46fc-928e-4fe7803d480f - example of uuid


class FormField(models.Model):
    inn_photo = models.ImageField(upload_to=PICTURES_FOLDER)
    snils_photo = models.ImageField(upload_to=PICTURES_FOLDER)

    full_name = models.TextField(default=None, null=True)
    date_of_birthday = models.DateField(default=None, null=True)

    gender_gender = models.TextField(choices=genders, default=None, null=True)
    inn_number = models.IntegerField(default=None, null=True)
    snils_number = models.IntegerField(default=None, null=True)

    passport_series_and_number = models.IntegerField(default=None, null=True)
    passport_issued_by = models.TextField(default=None, null=True)
    passport_date_of_issue = models.DateField(default=None, null=True)
    passport_division_code = models.IntegerField(default=None, null=True)
    passport_registered_address = models.TextField(default=None, null=True)
    passport_photo1 = models.ImageField(default=None, null=True)
    passport_photo2 = models.ImageField(default=None, null=True)

    place_of_birthday = models.TextField(default=None, null=True)
    citizenship = models.TextField(default=None, null=True)
    address_of_residence = models.TextField(default=None, null=True)
    is_civil_servant = models.BooleanField(default=None, null=True)
    date_of_vaccination = models.DateField(default=None, null=True)
    education = models.TextField(default=None, null=True)

    grade = models.IntegerField(default=None, null=True)
    salary = models.IntegerField(default=None, null=True)
    premium = models.IntegerField(default=None, null=True)
    job_descriptions = models.TextField(default=None, null=True)
    mvo = models.IntegerField(default=None, null=True)
    quarterly_option = models.IntegerField(default=None, null=True)
    annual_option = models.IntegerField(default=None, null=True)
    three_year_option = models.IntegerField(default=None, null=True)
    cash_year_content = models.IntegerField(default=None, null=True)
    cash_month_content = models.IntegerField(default=None, null=True)
    cash_year_without_option_content = models.IntegerField(default=None, null=True)
    cash_month_without_option_content = models.IntegerField(default=None, null=True)
    department = models.TextField(default=None, null=True)
    module = models.TextField(default=None, null=True)
    position = models.TextField(default=None, null=True)
    housing = models.TextField(default=None, null=True)

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
