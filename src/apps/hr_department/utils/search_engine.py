# django orm search by full_name in models DraftEmployeeInformation and ServerEmployeeInformation
from django.db.models import QuerySet

from apps.hr_department.models import ServerEmployeeInformation


def search_by_full_name(full_name: str) -> QuerySet[ServerEmployeeInformation]:
    server_employee_information = ServerEmployeeInformation.objects.filter(full_name=full_name)
    return server_employee_information
