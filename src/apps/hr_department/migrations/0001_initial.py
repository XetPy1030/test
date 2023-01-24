# Generated by Django 3.2.15 on 2023-01-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DraftEmployeeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn_photo', models.ImageField(upload_to='./pictures')),
                ('snils_photo', models.ImageField(upload_to='./pictures')),
                ('full_name', models.TextField(default=None, null=True)),
                ('date_of_birthday', models.DateField(default=None, null=True)),
                ('gender_gender', models.TextField(choices=[('MALE', 'Муж'), ('FEMALE', 'Жен')], default=None, null=True)),
                ('inn_number', models.TextField(default=None, null=True)),
                ('snils_number', models.IntegerField(default=None, null=True)),
                ('passport_series_and_number', models.IntegerField(default=None, null=True)),
                ('passport_issued_by', models.TextField(default=None, null=True)),
                ('passport_date_of_issue', models.DateField(default=None, null=True)),
                ('passport_division_code', models.IntegerField(default=None, null=True)),
                ('passport_registered_address', models.TextField(default=None, null=True)),
                ('passport_photo1', models.ImageField(default=None, null=True, upload_to='')),
                ('passport_photo2', models.ImageField(default=None, null=True, upload_to='')),
                ('place_of_birthday', models.TextField(default=None, null=True)),
                ('citizenship', models.TextField(default=None, null=True)),
                ('address_of_residence', models.TextField(default=None, null=True)),
                ('is_civil_servant', models.BooleanField(default=None, null=True)),
                ('date_of_vaccination', models.DateField(default=None, null=True)),
                ('education', models.TextField(default=None, null=True)),
                ('grade', models.IntegerField(default=None, null=True)),
                ('salary', models.IntegerField(default=None, null=True)),
                ('premium', models.IntegerField(default=None, null=True)),
                ('job_descriptions', models.TextField(default=None, null=True)),
                ('mvo', models.IntegerField(default=None, null=True)),
                ('quarterly_option', models.IntegerField(default=None, null=True)),
                ('annual_option', models.IntegerField(default=None, null=True)),
                ('three_year_option', models.IntegerField(default=None, null=True)),
                ('cash_year_content', models.IntegerField(default=None, null=True)),
                ('cash_month_content', models.IntegerField(default=None, null=True)),
                ('cash_year_without_option_content', models.IntegerField(default=None, null=True)),
                ('cash_month_without_option_content', models.IntegerField(default=None, null=True)),
                ('department', models.TextField(default=None, null=True)),
                ('module', models.TextField(default=None, null=True)),
                ('position', models.TextField(default=None, null=True)),
                ('housing', models.TextField(default=None, null=True)),
                ('is_checked', models.BooleanField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.TextField()),
                ('owner_id', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServerEmployeeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn_photo', models.ImageField(upload_to='./pictures')),
                ('snils_photo', models.ImageField(upload_to='./pictures')),
                ('full_name', models.TextField(default=None, null=True)),
                ('date_of_birthday', models.DateField(default=None, null=True)),
                ('gender_gender', models.TextField(choices=[('MALE', 'Муж'), ('FEMALE', 'Жен')], default=None, null=True)),
                ('inn_number', models.TextField(default=None, null=True)),
                ('snils_number', models.IntegerField(default=None, null=True)),
                ('passport_series_and_number', models.IntegerField(default=None, null=True)),
                ('passport_issued_by', models.TextField(default=None, null=True)),
                ('passport_date_of_issue', models.DateField(default=None, null=True)),
                ('passport_division_code', models.IntegerField(default=None, null=True)),
                ('passport_registered_address', models.TextField(default=None, null=True)),
                ('passport_photo1', models.ImageField(default=None, null=True, upload_to='')),
                ('passport_photo2', models.ImageField(default=None, null=True, upload_to='')),
                ('place_of_birthday', models.TextField(default=None, null=True)),
                ('citizenship', models.TextField(default=None, null=True)),
                ('address_of_residence', models.TextField(default=None, null=True)),
                ('is_civil_servant', models.BooleanField(default=None, null=True)),
                ('date_of_vaccination', models.DateField(default=None, null=True)),
                ('education', models.TextField(default=None, null=True)),
                ('grade', models.IntegerField(default=None, null=True)),
                ('salary', models.IntegerField(default=None, null=True)),
                ('premium', models.IntegerField(default=None, null=True)),
                ('job_descriptions', models.TextField(default=None, null=True)),
                ('mvo', models.IntegerField(default=None, null=True)),
                ('quarterly_option', models.IntegerField(default=None, null=True)),
                ('annual_option', models.IntegerField(default=None, null=True)),
                ('three_year_option', models.IntegerField(default=None, null=True)),
                ('cash_year_content', models.IntegerField(default=None, null=True)),
                ('cash_month_content', models.IntegerField(default=None, null=True)),
                ('cash_year_without_option_content', models.IntegerField(default=None, null=True)),
                ('cash_month_without_option_content', models.IntegerField(default=None, null=True)),
                ('department', models.TextField(default=None, null=True)),
                ('module', models.TextField(default=None, null=True)),
                ('position', models.TextField(default=None, null=True)),
                ('housing', models.TextField(default=None, null=True)),
                ('is_checked', models.BooleanField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]