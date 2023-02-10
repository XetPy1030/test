# Generated by Django 4.1.6 on 2023-02-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0003_remove_draftemployeeinformation_childrens_birth_certificates_date_of_birthday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(default=None, null=True)),
                ('date_of_birthday', models.DateField(default=None, null=True)),
                ('relation_degree', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_type', models.TextField(default=None, null=True)),
                ('educational_institution_name', models.TextField(default=None, null=True)),
                ('speciality', models.TextField(default=None, null=True)),
                ('qualification', models.TextField(default=None, null=True)),
                ('series_and_number', models.TextField(default=None, null=True)),
                ('date_of_issue', models.DateField(default=None, null=True)),
                ('photo', models.ImageField(default=None, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='draftemployeeinformation',
            name='childrens',
        ),
        migrations.RemoveField(
            model_name='draftemployeeinformation',
            name='education',
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='military_document_fitness',
            field=models.TextField(default=None, null=True),
        ),
        migrations.RemoveField(
            model_name='serveremployeeinformation',
            name='childrens',
        ),
        migrations.RemoveField(
            model_name='serveremployeeinformation',
            name='education',
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='military_document_fitness',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='draftemployeeinformation',
            name='childrens',
            field=models.ManyToManyField(default=None, null=True, to='hr_department.children'),
        ),
        migrations.AddField(
            model_name='draftemployeeinformation',
            name='education',
            field=models.ManyToManyField(default=None, null=True, to='hr_department.education'),
        ),
        migrations.AddField(
            model_name='serveremployeeinformation',
            name='childrens',
            field=models.ManyToManyField(default=None, null=True, to='hr_department.children'),
        ),
        migrations.AddField(
            model_name='serveremployeeinformation',
            name='education',
            field=models.ManyToManyField(default=None, null=True, to='hr_department.education'),
        ),
    ]
