import json

from django.http import HttpResponse

from apps.hr_department.models import DraftEmployeeInformation, ServerEmployeeInformation
from apps.hr_department.serializers.serializers import UserDraftSerializer
from apps.hr_department.views.errors import RequiredError, UserIsNotEditable


def get_user_id(request_data=None, request_get_data=None, request_headers=None):
    if request_data and 'user_id' in request_data:
        return request_data['user_id']
    if request_get_data and 'user_id' in request_get_data:
        return request_get_data['user_id']
    if request_headers and 'Authorization' in request_headers:
        return request_headers['Authorization']
    raise RequiredError()


def delete_drafts(user_id):
    models = DraftEmployeeInformation.objects.filter(user_id=user_id, owner_id=user_id)
    if models.exists():
        models.delete()


def delete_server_saves(user_id):
    models = ServerEmployeeInformation.objects.filter(user_id=user_id)
    if models.exists():
        models.delete()


def user_is_editable(user_id):
    try:
        user = ServerEmployeeInformation.objects.get(user_id=user_id)
        if not user.is_editable:
            return False
    except ServerEmployeeInformation.DoesNotExist:
        pass
    return True


def handler_all(request, model, serializer):
    if request.GET['all'] != 'true':
        return HttpResponse({'error': 'all must be true'}, status=401)
    models = model.objects.all()
    serializer = serializer(models, many=True)
    json_data = json.dumps(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
