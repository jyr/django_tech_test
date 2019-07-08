import threading

from apps.utils import tenant_db_from_request

THREAD_LOCAL = threading.local()

class RouterMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db_by_http_method = tenant_db_from_request(request)
        setattr(THREAD_LOCAL, "DB", db_by_http_method)

        return self.get_response(request)


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)
