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
    'passport__photos',
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

]



fields_frontend_to_backend = {
    "fullName": "full_name",
    "dateOfBirth": "date_of_birthday",
}


class EmployeeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        fields = 'all'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['name'] = ret.pop('employee_name')
        ret['age'] = ret.pop('employee_age')
        ret['salary'] = ret.pop('employee_salary')

        return ret
