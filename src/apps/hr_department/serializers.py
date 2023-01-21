from rest_framework import serializers

from apps.hr_department.models import EmployeeInformation

fields_frontend = [
    'full_name__full_name',
    'date_of_birthday__date',
    'gender__gender',
    'inn__number',
    'inn__photo',
    'snils__number',
    'snils__photo',
    'passport__series_and_number',
    'passport__issued_by',
    'passport__date_of_issue',
    'passport__division_code',
    'passport__registered_address',
    'passport__reversal',
    'passport__registration',
    'place_of_birthday__place',
    'citizenship__citizenship',
    'address_of_residence__address',
    'is_civil_servant__is_civil_servant',
    'date_of_vaccination__date',
    'education__education',
    'grade__grade',
    'salary__salary',
    'premium__premium',
    'job_descriptions__descriptions',
    'mvo__mvo',
    'options__quarterly_option',
    'options__annual_option',
    'options__three_year_option',
    'сash_content__cash_year__content',
    'сash_content__cash_month__content',
    'сash_content__cashyear_without_option__content',
    'сash_content__cash_month_without_option__content',
    'department__department',
    'module__module',
    'position__position',
    'housing__housing',
]

fields_backend = [
    'full_name',
    'date_of_birthday',
    'gender_gender',
    'inn_number',
    'inn_photo',
    'snils_number',
    'snils_photo',
    'passport_series_and_number',
    'passport_issued_by',
    'passport_date_of_issue',
    'passport_division_code',
    'passport_registered_address',
    'passport_photos',
    'place_of_birthday',
    'citizenship',
    'address_of_residence',
    'is_civil_servant',
    'date_of_vaccination',
    'education',
    'grade',
    'salary',
    'premium',
    'job_descriptions',
    'mvo',
    'quarterly_option',
    'annual_option',
    'three_year_option',
    'cash_year_content',
    'cash_month_content',
    'cashyear_without_option_content',
    'cash_month_without_option_content',
    'department',
    'module',
    'position',
    'housing'
]

date_fields = [
    'date_of_birthday',
    'date_of_issue',
    'date_of_vaccination',
    'passport_date_of_issue',
]

fields_frontend_to_backend = {
    key: value for key, value in zip(fields_frontend, fields_backend)
}


def get_field_name(field):
    return fields_frontend_to_backend.get(field, field)


def reformat_date_fields(data):
    for field in date_fields:
        if field in data:
            data[field] = data[field].split('T')[0]
            data[field] = data[field].replace('.', '-')


def reformat_passport_number(data):
    if 'passport_series_and_number' in data:
        passport_number = data['passport_series_and_number'].replace(' ', '')
        data['passport_series_and_number'] = ''.join(passport_number)


def reformat_snils_number(data):
    if 'snils_number' in data:
        snils_number = data['snils_number'].replace(' ', '')
        snils_number = snils_number.replace('-', '')
        data['snils_number'] = ''.join(snils_number)


def reformat_passport_division_code(data):
    if 'passport_division_code' in data:
        passport_division_code = data['passport_division_code'].replace('-', '')
        data['passport_division_code'] = ''.join(passport_division_code)


def reformat_fields(data):
    reformat_date_fields(data)
    reformat_passport_number(data)
    reformat_snils_number(data)
    reformat_passport_division_code(data)


class EmployeeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        fields = '__all__'
        validators = [
            ...
        ]

    def to_internal_value(self, data):
        data = {
            get_field_name(key): value for key, value in data.items()
        }

        reformat_fields(data)

        return super().to_internal_value(data)
