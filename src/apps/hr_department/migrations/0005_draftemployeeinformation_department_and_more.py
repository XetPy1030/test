# Generated by Django 4.1.6 on 2023-02-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0004_alter_draftemployeeinformation_im_foreigner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftemployeeinformation',
            name='department',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='draftemployeeinformation',
            name='supervisor',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='serveremployeeinformation',
            name='department',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='serveremployeeinformation',
            name='supervisor',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='children',
            name='full_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='children',
            name='relation_degree',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='addresses_address_for_information',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='addresses_address_outside_russia',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='citizenship',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='email',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='full_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='gender',
            field=models.TextField(blank=True, choices=[('male', '??????'), ('female', '??????')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='inn_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='married_status_full_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='married_status_relation_degree',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='passport_division_code',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='passport_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='passport_registered_address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='passport_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='patent_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='patent_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='phone_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='place_of_birthday',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='residence_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='residence_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='snils_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='status',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='status_of_the_insured_person_status',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='temporary_residence_permit_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='temporary_residence_permit_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_di_award',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_mbo_award_quarter',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_monthly_mbo_award',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_quarterly_option',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_quasi_option',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_salary',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='wage_yearly_option',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='work_permit_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftemployeeinformation',
            name='work_permit_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='education_type',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='educational_institution_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='language_proficiency',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='qualification',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='speciality',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='addresses_address_for_information',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='addresses_address_outside_russia',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='citizenship',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='email',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='full_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='gender',
            field=models.TextField(blank=True, choices=[('male', '??????'), ('female', '??????')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='inn_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='married_status_full_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='married_status_relation_degree',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='passport_division_code',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='passport_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='passport_registered_address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='passport_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='patent_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='patent_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='phone_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='place_of_birthday',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='residence_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='residence_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='snils_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='status',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='status_of_the_insured_person_status',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='temporary_residence_permit_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='temporary_residence_permit_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_di_award',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_mbo_award_quarter',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_monthly_mbo_award',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_quarterly_option',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_quasi_option',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_salary',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='wage_yearly_option',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='work_permit_issued_by',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='serveremployeeinformation',
            name='work_permit_series_and_number',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
