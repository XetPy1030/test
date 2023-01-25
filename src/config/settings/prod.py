# Elasticsearch
# https://django-elasticsearch-dsl.readthedocs.io/en/latest/settings.html
from config.env_variables import DATABASE_PASSWORD

ELASTIC_SEARCH_HOST = 'es01'
ELASTIC_SEARCH_PORT = 9200

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'es01:9200'
    },
}

# DATABASES = {
#     'default': {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "hrdb",
#         "USER": "master",
#         "PASSWORD": "9D9*1$!kVZRo",
#         "HOST": "postgres",
#         "PORT": 5432,
#     }
# }
