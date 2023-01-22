# django orm search by full_name in models DraftEmployeeInformation and ServerEmployeeInformation
from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation


def search_by_full_name(full_name):
    draft_employee_information = DraftEmployeeInformation.objects.filter(full_name=full_name)
    server_employee_information = ServerEmployeeInformation.objects.filter(full_name=full_name)
    return draft_employee_information, server_employee_information
