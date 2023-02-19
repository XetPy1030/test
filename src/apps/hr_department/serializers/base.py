import os

from django.http import QueryDict
from rest_framework import serializers

from apps.hr_department.models import Children, Education, ServerEmployeeInformation
from apps.hr_department.serializers.utils.fields import fields_frontend_to_backend, fields_backend_to_frontend
from apps.hr_department.serializers.utils.reformaters import reformat_frontend_fields, reformat_iter_frontend_fields
from apps.hr_department.serializers.utils.status import calculate_status
from config import settings


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ("full_name", "date_of_birthday", "relation_degree")

    def to_internal_value(self, data):
        if isinstance(data, QueryDict):
            data = data.dict()

        for key, value in data.items():
            if value == 'null' or value == 'undefined':
                data[key] = None

        return super().to_internal_value(data)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "education_type",
            "educational_institution_name",
            "speciality",
            "qualification",
            "series_and_number",
            "date_of_issue",
            "date_range_of_education",
            "language_proficiency",
            "photo"
        )

    def to_internal_value(self, data):
        if isinstance(data, QueryDict):
            data = data.dict()

        for key, value in data.items():
            if value == 'null' or value == 'undefined':
                data[key] = None

        return super().to_internal_value(data)


class BaseMeta:
    fields = '__all__'
    validator_classes = []
    validators = [
        validator_classes
    ]


class BaseSerializer(serializers.ModelSerializer):
    children = ChildrenSerializer(many=True, required=False)
    education = EducationSerializer(many=True, required=False)

    def create(self, validated_data):
        childrens = validated_data.pop('children', [])
        education = validated_data.pop('education', [])
        instance = super().create(validated_data)

        for children in childrens:
            children_model = Children.objects.create(**children)
            instance.children.add(children_model)

        for edu in education:
            edu_model = Education.objects.create(**edu)
            instance.education.add(edu_model)

        return instance

    def update(self, instance, validated_data):
        childrens = validated_data.pop('children', [])
        education = validated_data.pop('education', [])
        instance = super().update(instance, validated_data)

        for children in childrens:
            children_model = Children.objects.create(**children)
            instance.children.add(children_model)

        for edu in education:
            edu_model = Education.objects.create(**edu)
            instance.education.add(edu_model)

        return instance

    def to_internal_value(self, data: QueryDict):
        if isinstance(data, QueryDict):
            data = data.dict()

        reformat_iter_frontend_fields(data)

        reformat_frontend_fields(data)

        for key, value in data.items():
            if value == 'null' or value == 'undefined':
                data[key] = None

        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data = data.copy()

        if isinstance(self.Meta.model, ServerEmployeeInformation) or self.Meta.model == ServerEmployeeInformation:
            status = calculate_status(instance.user_id)
            data['status'] = status

        for image in data:
            if 'photo' in image:
                if data[image]:
                    path = os.path.join(settings.MEDIA_ROOT, data[image])
                    if not os.path.isfile(path):
                        continue

        return data

    @staticmethod
    def get_field_frontend_name(field):
        return fields_backend_to_frontend.get(field, field)

    @staticmethod
    def get_field_backend_name(field):
        return fields_frontend_to_backend.get(field, field)

    def get_status(self):
        user_id = self.validated_data.get('user_id')
        return calculate_status(user_id)
