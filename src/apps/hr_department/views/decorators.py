from functools import wraps

from apps.hr_department.views.errors import RequiredError
from apps.hr_department.views.sends import not_found_params
from apps.hr_department.views.utils import get_user_id, handler_all, get_owner_id


def add_user_id(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            user_id = get_user_id(request_data=request.data, request_get_data=request.GET,
                                  request_headers=request.headers)
        except RequiredError:
            return not_found_params(request, 'user_id')
        clone_request_data = request.data.copy()
        clone_request_data['user_id'] = user_id
        request.clone_data = clone_request_data
        return func(request, *args, user_id, **kwargs)

    return wrapper


def add_owner_id(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            owner_id = get_owner_id(request_data=request.data, request_get_data=request.GET,
                                    request_headers=request.headers)
        except RequiredError:
            return not_found_params(request, 'owner_id')
        clone_request_data = request.data.copy()
        clone_request_data['owner_id'] = owner_id
        request.clone_data = clone_request_data
        return func(request, *args, owner_id, **kwargs)

    return wrapper


def handler_all_decorator(models, serializer):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if 'all' in request.GET:
                return handler_all(request, models, serializer)
            return func(request, *args, **kwargs)

        return wrapper

    return decorator
