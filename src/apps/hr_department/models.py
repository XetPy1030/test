from django.db import models

from src.config.env_variables import pictures_folder


# Create your models here.

class EmployeeInformation(models.Model):
    user_id = models.BigIntegerField()
    save_as_draft = models.BooleanField()

    full_name_full_name = models.TextField(default=None)
    date_of_birthday_date = models.DateField(default=None)
    genders = (
        ("MALE", "Муж"),
        ("FEMALE", "Жен")
    )
    gender_gender = models.TextField(choices=genders, default=None)
    inn_number = models.IntegerField(default=None)
    inn_photo = models.ImageField(upload_to=pictures_folder)
    snils_number = models.IntegerField(default=None)
    snils_photo = models.ImageField(upload_to=pictures_folder)

    passport_series_and_number = models.IntegerField(default=None)
    passport_issued_by = models.TextField(default=None)
    passport_date_of_issue = models.DateField(default=None)
    passport_division_code = models.IntegerField(default=None)
    passport_registered_address = models.TextField(default=None)
    passport_photos = models.ImageField(default=None)

    place_of_birthday_place = models.TextField(default=None)
    citizenship_citizenship = models.TextField(default=None)
    address_of_residence_address = models.TextField(default=None)
    is_civil_servant = models.BooleanField(default=None)
    date_of_vaccination_date = models.DateField(default=None)
    education_education = models.TextField(default=None)

    grade_grade = models.IntegerField(default=None)
    salary_salary = models.IntegerField(default=None)
    premium_premium = models.IntegerField(default=None)
    job_descriptions_descriptions = models.TextField(default=None)
    mvo_mvo = models.IntegerField(default=None)
    options_quarterly_option = models.IntegerField(default=None)
    options_annual_option = models.IntegerField(default=None)
    options_three_year_option = models.IntegerField(default=None)
    cash_content_cash_year_content = models.IntegerField(default=None)
    cash_content_cash_month_content = models.IntegerField(default=None)
    cash_content_cashyear_without_option_content = models.IntegerField(default=None)
    cash_content_cash_month_without_option_content = models.IntegerField(default=None)
    department_department = models.TextField(default=None)
    module_module = models.TextField(default=None)
    position_position = models.TextField(default=None)
    housing_housing = models.TextField(default=None)


