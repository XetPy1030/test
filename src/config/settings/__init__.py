from .base import *
from ..env_variables import MODE

if MODE != 'local':
    from .prod import *
    INSTALLED_APPS += PROD_APPS

