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
    'full_name': 'Богомолова Надежда Семёновна',
    'date_of_birthday': '1990-01-01T00:00:00',
    '0__children_full_name': 'Богомолова Надежда Семёновна',
    '1__children_full_name': 'Богомолова Надежда Семёновна',
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

    def testChildrenUpdate(self):
        response = self.client.post(self.admin_save_url.format(1), data_for_serializer)
        self.assertEqual(response.status_code, 201)


        # response = self.client.get(self.admin_save_url.format(1))
        # print(response.content)

        response = self.client.post(self.admin_save_url.format(1), {
            'full_name': 'awdwad'
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.get(self.admin_save_url.format(1))
        self.assertEqual(json.loads(response.content)['children'].__len__(), 2)

