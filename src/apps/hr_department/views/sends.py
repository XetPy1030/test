import json

from django.http import HttpResponse


def base_send(request, data, status):
    return HttpResponse(json.dumps(data), status=status, content_type='application/json')


def not_found_params(request, params):
    return base_send(request, {'error': 'not found params: {}'.format(params)}, 401)


def not_valid_data(request, errors):
    return base_send(request, {'error': 'data in request not valid', 'errors': errors}, 400)


def success_save(request):
    return base_send(request, {'success': True}, 201)


def not_found(request):
    return base_send(request, {'success': False}, 404)


def send_data(request, data):
    return base_send(request, data, 200)


def not_permission_save(request):
    return base_send(request, {'error': 'user is not editable'}, 400)
