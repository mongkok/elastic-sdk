

def test_client_info(client):
    assert 'name' in client.es.info()


def test_search_create_index(client):
    response = client.search().idx(
        id='test.id',
        body={},
        doc_type='doc.test')

    assert response['_type'] == 'doc.test'


def test_search_create_index_with_prefix(client_prefix):
    response = client_prefix.user.idx(
        id='test.id',
        body={})

    assert response['_type'] == 'prefix.user'


def test_attr_create_index(client):
    response = client.user.idx(id='user.id', body={'username': 'me'})
    assert response['_type'] == 'user'


def test_client_get(client, index):
    assert client.get(id=index['_id'])['test']


def test_client_delete(client):
    index = client.fixtures.idx(id='fixture.tmp', body={})
    response = client.delete(doc_name='fixtures', id=index['_id'])
    assert response['result'] == 'deleted'


def test_search_all(client):
    assert client.fixtures.all().hits().total


def test_search_q(client):
    assert client.fixtures.q(test=True).hits().total


def test_search_exists(client):
    assert client.fixtures.exists(field='test').hits().total


def test_search_multi_match(client):
    fields = ['title', 'description']
    response = client.fixtures.multi_match(
        q='the',
        fields=fields,
    ).hits()

    assert set(response.hits[0]['highlight']) == set(fields)
