DEBUG = True

ALLOWED_HOSTS = ["*"]

ELASTIC_SEARCH_HOST = 'es01'
ELASTIC_SEARCH_PORT = 9200

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'localdb.sqlite3',
    }
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'es01:9200'
    },
}

CORS_ORIGIN_ALLOW_ALL = True
