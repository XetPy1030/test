from apps.hr_department.serializers.utils.status import calculate_status
from apps.hr_department.views.admin import SearchHandler, AdminSaveHandler, AdminDraftHandler
from apps.hr_department.views.user import UserSaveHandler, UserDraftHandler
from config import settings
import os

from config.env_variables import MODE

if MODE != 'local':
    from apps.hr_department.views.search import ServerSearchEmployeeInformationDocumentViewSet, \
        SpreadSheetSearchEmployeeInformationDocumentViewSet

from django.http import HttpResponse


def get_type_of_img(path_image):
    if path_image.endswith('.png'):
        return 'image/png'
    elif path_image.endswith('.jpg'):
        return 'image/jpeg'
    elif path_image.endswith('.jpeg'):
        return 'image/jpeg'
    elif path_image.endswith('.gif'):
        return 'image/gif'
    else:
        return 'image/png'


def image_handler(request):
    path_image = settings.MEDIA_ROOT + request.GET['path']
    content_type = get_type_of_img(path_image)
    try:
        with open(path_image, 'rb') as f:
            data = f.read()
        return HttpResponse(data, content_type=content_type)
    except FileNotFoundError:
        return HttpResponse({'error': 'image not found'}, status=404)


def status_handler(request):
    user_id = request.GET['user_id']
    status = calculate_status(user_id)
    return HttpResponse({"status": status}, content_type='application/json')
