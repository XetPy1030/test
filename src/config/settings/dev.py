DEBUG = True

ALLOWED_HOSTS = ["*"]

ELASTIC_SEARCH_HOST = 'es01'
ELASTIC_SEARCH_PORT = 9200

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'es01:9200',
        'timeout': 60,
    },
}



DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "hrdb",
        "USER": "master",
        "PASSWORD": "9D9*1$!kVZRo",
        "HOST": "postgres",
        "PORT": 5432,
    }
}

CORS_ORIGIN_ALLOW_ALL = True

MEDIA_ROOT = 'pictures'

APPS = [
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
]
