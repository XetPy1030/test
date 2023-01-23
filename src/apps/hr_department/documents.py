from .models import ServerEmployeeInformation, DraftEmployeeInformation
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


# Document class for the DraftEmployeeInformation model
@registry.register_document
class DraftEmployeeInformationDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'draftemployeeinformation'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = DraftEmployeeInformation
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'full_name',
        ]


# Document class for the ServerEmployeeInformation model
@registry.register_document
class ServerEmployeeInformationDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'serveremployeeinformation'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = ServerEmployeeInformation
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'full_name',
        ]
