from django.db import models

from config.env_variables import PICTURES_FOLDER

# Create your models here.

genders = (
        ("MALE", "Муж"),
        ("FEMALE", "Жен")
    )


class EmployeeInformation(models.Model):
    user_id = models.BigIntegerField()
    save_as_draft = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    full_name = models.TextField(default=None)
    date_of_birthday = models.DateField(default=None)

    gender_gender = models.TextField(choices=genders, default=None)
    inn_number = models.IntegerField(default=None)
    inn_photo = models.ImageField(upload_to=PICTURES_FOLDER)
    snils_number = models.IntegerField(default=None)
    snils_photo = models.ImageField(upload_to=PICTURES_FOLDER)

    passport_series_and_number = models.IntegerField(default=None)
    passport_issued_by = models.TextField(default=None)
    passport_date_of_issue = models.DateField(default=None)
    passport_division_code = models.IntegerField(default=None)
    passport_registered_address = models.TextField(default=None)
    passport_photo1 = models.ImageField(default=None)
    passport_photo2 = models.ImageField(default=None)


    place_of_birthday = models.TextField(default=None)
    citizenship = models.TextField(default=None)
    address_of_residence = models.TextField(default=None)
    is_civil_servant = models.BooleanField(default=None)
    date_of_vaccination = models.DateField(default=None)
    education = models.TextField(default=None)

    grade = models.IntegerField(default=None)
    salary = models.IntegerField(default=None)
    premium = models.IntegerField(default=None)
    job_descriptions = models.TextField(default=None)
    mvo = models.IntegerField(default=None)
    quarterly_option = models.IntegerField(default=None)
    annual_option = models.IntegerField(default=None)
    three_year_option = models.IntegerField(default=None)
    cash_year_content = models.IntegerField(default=None)
    cash_month_content = models.IntegerField(default=None)
    cashyear_without_option_content = models.IntegerField(default=None)
    cash_month_without_option_content = models.IntegerField(default=None)
    department = models.TextField(default=None)
    module = models.TextField(default=None)
    position = models.TextField(default=None)
    housing = models.TextField(default=None)


