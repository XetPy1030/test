import os

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.exceptions import ConnectionError
import pandas as pd
import time

# follow Mihai Todor's suggestion on https://stackoverflow.com/questions/48711455/create-dockerized-elasticsearch-index-using-a-python-script-running-in-docker/48712414#48712414
es = Elasticsearch(hosts=[{"host": "es01"}], retry_on_timeout=True)

for _ in range(100):
    try:
        # make sure the cluster is available
        es.cluster.health(wait_for_status="yellow")
    except ConnectionError:
        time.sleep(2)

os.system("python manage.py search_index --rebuild -f")