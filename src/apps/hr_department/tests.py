import base64
from io import BytesIO

import requests
from PIL import Image
from django.test import TestCase

from apps.hr_department.serializers.serializers import UserDraftEmployeeInformationSerializer


def get_base64_from_image(image_path: str):
    image = Image.open(open(image_path, 'rb'))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')


data_for_serializer = {
    'full_name__full_name': 'Иванов Иван Иванович',
    'date_of_birthday__date': '1990-01-01T00:00:00',  # '1990-01-01'
    'gender__gender': 'MALE',
    'inn__number': '123456789012',
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
    'inn__photo': get_base64_from_image('./apps/hr_department/tests/inn.jpg'),
    'snils__photo': get_base64_from_image('./apps/hr_department/tests/snils.jpg'),
    'passport__photo_reversal': get_base64_from_image('./apps/hr_department/tests/passport_reversal.jpg'),
    'passport__photo_registration': get_base64_from_image('./apps/hr_department/tests/passport_registration.jpg'),
}


class DraftEmployeeInformationTestCase(TestCase):
    def setUp(self):
        self.serializer = UserDraftEmployeeInformationSerializer(data=data_for_serializer)
        self.serializer.is_valid(raise_exception=True)

    def test_serializer_is_valid(self):
        self.assertTrue(self.serializer.is_valid())


class RequestsTestCase(TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/v1'

    def test_user_draft_post(self):
        response = requests.post(f'{self.url}/user/draft/', data=data_for_serializer)
        self.assertEqual(response.status_code, 201)

    def test_user_draft_get(self):
        response = requests.get(f'{self.url}/user/draft/', params={'jwt_token': '123'})
        self.assertEqual(response.status_code, 200)

    # def test_user_save_post(self):
    #     response = requests.post(f'{self.url}/user/save/', data=data_for_serializer)
    #     self.assertEqual(response.status_code, 201)

    # def test_user_save_get(self):
    #     response = requests.get(f'{self.url}/user/save/', params={'jwt_token': '123'})
    #     self.assertEqual(response.status_code, 200)
