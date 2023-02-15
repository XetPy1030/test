import base64
from io import BytesIO

from PIL import Image
from django.test import TestCase, Client

from apps.hr_department.documents.spreadSheet_search_document import SpreadSheetSearchEmployeeInformationDocument
from apps.hr_department.views import UserSaveHandler

def get_base64_from_image(image_path: str):
    image = Image.open(open(image_path, 'rb'))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')


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


class DraftEmployeeInformationTestCase(TestCase):
    def setUp(self):
        # Client with headers
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0', HTTP_HOST='localhost', user_id='1')
        self.user_save_url = '/api/v1/user/save/?user_id={}'
        self.user_draft_url = '/api/v1/user/draft/?user_id={}'
        self.admin_save_url = '/api/v1/admin/save/?user_id={}'
        self.admin_draft_url = '/api/v1/admin/draft/?user_id={}'

    def testSaveHandlers(self):
        response = self.client.post(self.user_save_url.format(1), data_for_serializer)
        self.assertEqual(response.status_code, 201)
        response = self.client.post(self.admin_save_url.format(1), data_for_serializer)
        self.assertEqual(response.status_code, 201)
        # get all field from SpreadSheetSearchEmployeeInformationDocument
        print(SpreadSheetSearchEmployeeInformationDocument._fields)