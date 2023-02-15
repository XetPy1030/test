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

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'ORDERING_PARAM': 'ordering',
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

APPS = [
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
]
