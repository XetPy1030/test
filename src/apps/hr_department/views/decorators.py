from functools import wraps

from apps.hr_department.views.errors import RequiredError
from apps.hr_department.views.utils import get_user_id, handler_all


def add_user_id(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            user_id = get_user_id(request_data=request.data, request_get_data=request.GET, request_headers=request.headers)
        except RequiredError:
            user_id = None
        clone_request_data = request.data.copy()
        clone_request_data['user_id'] = user_id
        request.clone_data = clone_request_data
        return func(request, *args, user_id, **kwargs)

    return wrapper


# decorator для обработки, есть ли в запросе all, если есть, то возвращаем все записи
#
def add_all(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if 'all' in request.GET:
            handler_all

        return func(request, *args, **kwargs)

    return wrapper
