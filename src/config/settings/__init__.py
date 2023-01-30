from .base import *
from ..env_variables import MODE

if MODE == 'local':
    from .local import *

elif MODE == 'production':
    from .prod import *

elif MODE == 'dev':
    from .dev import *
    # INSTALLED_APPS += APPS after rest_framework
    for i in APPS[::-1]:
        INSTALLED_APPS.insert(INSTALLED_APPS.index('rest_framework') + 1, i)

