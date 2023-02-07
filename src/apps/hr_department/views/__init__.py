from apps.hr_department.views.admin import SearchHandler, AdminSaveHandler, AdminDraftHandler
from apps.hr_department.views.user import UserSaveHandler, UserDraftHandler

from config.env_variables import MODE

if MODE != 'local':
    from apps.hr_department.views.search import ServerSearchEmployeeInformationDocumentViewSet

from django.http import HttpResponse


def test(request):
    return HttpResponse('test')
