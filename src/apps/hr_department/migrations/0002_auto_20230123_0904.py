# Generated by Django 3.2.15 on 2023-01-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='passport_division_code',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='snils_number',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='passport_division_code',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='snils_number',
            field=models.TextField(default=None, null=True),
        ),
    ]
