# from elasticsearch_dsl.query import Q


def test_client_info(client):
    assert 'name' in client.es.info()
