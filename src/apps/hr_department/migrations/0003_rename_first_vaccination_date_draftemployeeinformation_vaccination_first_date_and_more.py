# Generated by Django 4.1.6 on 2023-02-16 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0002_draftemployeeinformation_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='draftemployeeinformation',
            old_name='first_vaccination_date',
            new_name='vaccination_first_date',
        ),
        migrations.RenameField(
            model_name='draftemployeeinformation',
            old_name='second_vaccination_date',
            new_name='vaccination_second_date',
        ),
        migrations.RenameField(
            model_name='serveremployeeinformation',
            old_name='first_vaccination_date',
            new_name='vaccination_first_date',
        ),
        migrations.RenameField(
            model_name='serveremployeeinformation',
            old_name='second_vaccination_date',
            new_name='vaccination_second_date',
        ),
    ]
