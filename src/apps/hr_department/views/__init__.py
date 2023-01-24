from apps.hr_department.views.admin import SearchHandler
from apps.hr_department.views.user import UserSaveEmployeeDraftHandler, UserDraftEmployeeHandler
from config.env_variables import MODE

if MODE != 'local':
    from apps.hr_department.views.search import ServerSearchEmployeeInformationDocumentViewSet
