import os
from rest_framework import serializers

from apps.hr_department.models import Children, Education
from apps.hr_department.serializers.utils.fields import fields_frontend_to_backend, fields_backend_to_frontend
from apps.hr_department.serializers.utils.reformaters import reformat_frontend_fields, reformat_iter_frontend_fields
from config import settings


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ("full_name", "date_of_birthday", "relation_degree")


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("education_type", "educational_institution_name", "speciality", "qualification", "series_and_number")


class BaseSerializer(serializers.ModelSerializer):
    """
    childrens - ManyToManyField
    model - Children
    for example childrens = [ {'full_name': 'Ivanov Ivan Ivanovich', 'date_of_birthday': '1990-01-01', 'relation_degree': 'son'} ]
    ChildrenSerializer - serializer for model Children
    childrens = list[dict]
    create new if not exist
    """
    childrens = ChildrenSerializer(many=True, required=False)
    education = EducationSerializer(many=True, required=False)

    def create(self, validated_data):
        childrens = validated_data.pop('childrens', [])
        education = validated_data.pop('education', [])
        instance = super().create(validated_data)

        for children in childrens:
            children_model = Children.objects.create(**children)
            instance.childrens.add(children_model)

        for edu in education:
            edu_model = Education.objects.create(**edu)
            instance.education.add(edu_model)

        return instance

    def update(self, instance, validated_data):
        childrens = validated_data.pop('childrens', [])
        education = validated_data.pop('education', [])
        instance = super().update(instance, validated_data)

        for children in childrens:
            children_model = Children.objects.create(**children)
            instance.childrens.add(children_model)

        for edu in education:
            edu_model = Education.objects.create(**edu)
            instance.education.add(edu_model)

        return instance

    def to_internal_value(self, data):
        data = {
            self.get_field_backend_name(key): value for key, value in data.items()
        }
        reformat_iter_frontend_fields(data)

        reformat_frontend_fields(data)

        for key, value in data.items():
            if value == 'null' or value == 'undefined':
                data[key] = None

        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data = {
            self.get_field_frontend_name(key): value for key, value in data.items()
        }

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
