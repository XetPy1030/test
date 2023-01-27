from .base import *
from ..env_variables import MODE

if MODE == 'local':
    from .local import *

elif MODE == 'production':
    from .prod import *

elif MODE == 'dev':
    from .dev import *
