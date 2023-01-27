from config.env_variables import MODE
from .base import urlpatterns

if MODE == 'dev':
    from .server_search import urlpatterns as server_search_urlpatterns

    urlpatterns += server_search_urlpatterns
