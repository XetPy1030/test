from django.db import models

from src.config.env_variables import pictures_folder


# Create your models here.

class EmployeeInformation(models.Model):
    user_id = models.BigIntegerField()
    save_as_draft = models.BooleanField()

    full_name__full_name = models.TextField(default=None)
    date_of_birthday__date = models.DateField(default=None)
    genders = (
        ("MALE", "Муж"),
        ("FEMALE", "Жен")
    )
    gender__gender = models.TextField(choices=genders, default=None)
    inn__number = models.IntegerField(max_length=12, default=None)
    inn__photo = models.ImageField(upload_to=pictures_folder)
    snils__number = models.IntegerField(max_length=11, default=None)
    snils__photo = models.ImageField(upload_to=pictures_folder)

    passport__series_and_number = models.IntegerField(default=None)
    passport__issued_by = models.TextField(default=None)
    passport__date_of_issue = models.DateField(default=None)
    passport__division_code = models.IntegerField(default=None)
    passport__registered_address = models.TextField(default=None)
    passport__photos = models.ImageField(default=None)

    place_of_birthday__place = models.TextField(default=None)
    citizenship__citizenship = models.TextField(default=None)
    address_of_residence__address = models.TextField(default=None)
    is_civil_servant = models.BooleanField(default=None)
    date_of_vaccination__date = models.DateField(default=None)
    education__education = models.TextField(default=None)

    grade__grade = models.IntegerField(default=None)
    salary__salary = models.IntegerField(default=None)
    premium__premium = models.IntegerField(default=None)
    job_descriptions__descriptions = models.TextField(default=None)
    mvo__mvo = models.IntegerField(default=None)
    options__quarterly_option = models.IntegerField(default=None)
    options__annual_option = models.IntegerField(default=None)
    options__three_year_option = models.IntegerField(default=None)
    cash_content__cash_year__content = models.IntegerField(default=None)
    cash_content__cash_month__content = models.IntegerField(default=None)
    cash_content__cashyear_without_option__content = models.IntegerField(default=None)
    cash_content__cash_month_without_option__content = models.IntegerField(default=None)
    department__department = models.TextField(default=None)
    module__module = models.TextField(default=None)
    position__position = models.TextField(default=None)
    housing__housing = models.TextField(default=None)


