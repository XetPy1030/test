from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation
from config import settings


def calculate_check_not_is_server_model(user_id):
    is_draft_model: bool
    try:
        DraftEmployeeInformation.objects.get(user_id=user_id)
        is_draft_model = True
    except DraftEmployeeInformation.DoesNotExist:
        is_draft_model = False

    return "user_is_writing" if is_draft_model else "user_not_found"


def calculate_check_is_server_is_checked_model(data):
    is_editable = data['is_editable']
    return "user_is_rejected" if is_editable else "user_is_approved"


def calculate_check_is_server_is_not_checked_model(data):
    is_editable = data['is_editable']
    if is_editable:
        if settings.DEBUG:
            return "impossible_state"
        raise Exception(f"User is not checked but is editable: {data['user_id']}")
    return "user_sent"


def calculate_check_is_server_model(data):
    is_checked = data['is_checked']
    return calculate_check_is_server_is_checked_model(
        data) if is_checked else calculate_check_is_server_is_not_checked_model(data)


def calculate_status(user_id):
    is_server_model: bool
    try:
        model = ServerEmployeeInformation.objects.get(user_id=user_id)
        data = {
            'is_checked': model.is_checked,
            'is_editable': model.is_editable,
            'user_id': model.user_id,
        }
        is_server_model = True
    except ServerEmployeeInformation.DoesNotExist:
        is_server_model = False

    return calculate_check_is_server_model(data) if is_server_model else calculate_check_not_is_server_model(user_id)
