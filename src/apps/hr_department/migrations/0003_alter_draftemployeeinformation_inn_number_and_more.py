# Generated by Django 4.1.3 on 2023-01-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0002_draftemployeeinformation_serveremployeeinformation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='inn_number',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='inn_number',
            field=models.TextField(default=None, null=True),
        ),
    ]
