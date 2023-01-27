import base64
from io import BytesIO

from apps.hr_department.views.admin import SearchHandler
from apps.hr_department.views.user import UserSaveEmployeeHandler, UserDraftEmployeeHandler
from config.env_variables import MODE

if MODE != 'local':
    from apps.hr_department.views.search import ServerSearchEmployeeInformationDocumentViewSet


from ..models import ServerEmployeeInformation
from django.http import HttpResponse
from PIL import Image
def test(requests):
    us = ServerEmployeeInformation.objects.all()[0].passport_reversal_photo
    # open us image in pillow


