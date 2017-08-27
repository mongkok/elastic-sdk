from elasticsearch_dsl.query import Q


def test_client_info(client):
    print(client.es.info())
