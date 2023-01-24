from .base import *
from ..env_variables import MODE

if MODE != 'local':
    from .prod import *
    INSTALLED_APPS.extend(PROD_APPS)
