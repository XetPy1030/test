import base64
import json
from io import BytesIO
from django.test import TestCase

import requests
from PIL import Image
from django.test import TestCase

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftSerializer, \
    UserSaveSerializer


#
# from apps.hr_department.models import DraftEmployeeInformation
# from apps.hr_department.serializers import DraftEmployeeInformationSerializer


def get_base64_from_image(image_path: str):
    image = Image.open(open(image_path, 'rb'))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')

# Абрамова Милана Максимовна
# Акимов Мирослав Владиславович
# Алексеева Елена Романовна
# Алексеева Василиса Леонидовна
# Андреев Платон Леонидович
# Андреев Михаил Вадимович
# Афанасьева Вероника Фёдоровна
# Боброва Анна Михайловна
# Богомолова Надежда Семёновна
# Болдырев Дмитрий Львович
# Борисов Виктор Андреевич
# Борисов Лев Романович
# Виноградова Дарья Петровна
# Волкова Елизавета Андреевна
# Воронин Захар Тимофеевич


data_for_serializer = {
    'full_name__full_name': 'Богомолова Надежда Семёновна',
    'date_of_birthday__date': '1990-01-01T00:00:00',
    'gender__gender': 'male',
    'inn__number': '822199435930',
    'snils__number': '123-456-789 01',
    'passport__series_and_number': '1234 567890',
    'passport__issued_by': 'ОВД г. Москвы',
    'passport__date_of_issue': '2010-01-01T00:00:00',
    'passport__division_code': '123-456',
    'passport__registered_address': 'г. Москва, ул. Ленина, д. 1',
    'place_of_birthday__place': 'г. Москва',
    'citizenship__citizenship': 'Россия',
    'address_of_residence__address': 'г. Москва, ул. Ленина, д. 1',
    'is_civil_servant__is_civil_servant': True,
    'date_of_vaccination__date': '2010-01-01T00:00:00',
    'education__education': 'Высшее',
    'grade__grade': '1',
    'salary__salary': '100000',
    'premium__premium': '10000',
    'job_descriptions__descriptions': 'Разработчик',
    'mvo__mvo': '1',
    'options__quarterly_option': '1',
    'options__annual_option': '1',
    'options__three_year_option': '1',
    'сash_content__cash_year__content': '100000',
    'сash_content__cash_month__content': '10000',
    'сash_content__cashyear_without_option__content': '100000',
    'сash_content__cash_month_without_option__content': '10000',
    'department__department': 'Отдел разработки',
    'module__module': 'Модуль разработки',
    'position__position': 'Разработчик',
    'housing__housing': '1',
    # 'inn__photo': get_base64_from_image('./apps/hr_department/tests/inn.jpg'),
    # 'snils__photo': get_base64_from_image('./apps/hr_department/tests/snils.jpg'),
    # 'passport__photo_reversal': get_base64_from_image('./apps/hr_department/tests/passport_reversal.jpg'),
    # 'passport__photo_registration': get_base64_from_image('./apps/hr_department/tests/passport_registration.jpg'),
}

# json_object = json.dumps(data_for_serializer, indent = 4)
# text_file = open("./sample.json", "w")
# n = text_file.write(json_object)
# text_file.close()


class DraftEmployeeInformationTestCase(TestCase):
    def setUp(self):
        ...

    # def testRequest(self):
    #     clone_data_for_serializer = data_for_serializer.copy()
    #     clone_data_for_serializer['user_id'] = 1
    #     response = requests.post('http://127.0.0.1:8000/api/v1/user/draft/', data=clone_data_for_serializer)
    #     self.assertEqual(response.status_code, 201)

    def testDraftEmployeeInformation(self):
        clone_data_for_serializer = data_for_serializer.copy()
        clone_data_for_serializer['user_id'] = 1
        clone_data_for_serializer['owner_id'] = 1
        serializer = UserDraftSerializer(data=clone_data_for_serializer)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()
        self.assertEqual(DraftEmployeeInformation.objects.count(), 1)
        self.assertEqual(DraftEmployeeInformation.objects.get().user_id, '1')

    def testDraftEmployeeInformationWithoutUserId(self):
        clone_data_for_serializer = data_for_serializer.copy()
        serializer = UserDraftSerializer(data=clone_data_for_serializer)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'user_id': ['This field is required.'], 'owner_id': ['This field is required.']})

    def testUserSave(self):
        clone_data_for_serializer = data_for_serializer.copy()
        clone_data_for_serializer['user_id'] = 1
        clone_data_for_serializer['owner_id'] = 1
        serializer = UserSaveSerializer(data=clone_data_for_serializer)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(ServerEmployeeInformation.objects.count(), 1)
        self.assertEqual(ServerEmployeeInformation.objects.get().id, 1)

    def testUserSaveWithoutUserId(self):
        clone_data_for_serializer = data_for_serializer.copy()
        serializer = UserSaveSerializer(data=clone_data_for_serializer)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'user_id': ['This field is required.']})


def file_to_json(file):
    with open(file, 'r') as f:
        return json.load(f)
