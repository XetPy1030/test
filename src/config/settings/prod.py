# Elasticsearch
# https://django-elasticsearch-dsl.readthedocs.io/en/latest/settings.html
from config.env_variables import DATABASE_PASSWORD

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

PROD_APPS = [
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
]

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "hrdb",
        "USER": "master",
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": "postgres",
        "PORT": 5432,
    }
}
