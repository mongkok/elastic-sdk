import pytest

import elastic_sdk


@pytest.fixture(scope='module')
def client(request):
    return elastic_sdk.Client(index_name='test')


@pytest.fixture(scope='module')
def client_prefix(request):
    return elastic_sdk.Client(index_name='test', doc_prefix='prefix')


@pytest.fixture(scope='module')
def index(request, client):
    return client.fixtures.idx(
        id='fixture_id',
        body={
            'test': True,
            'title': 'this is the title',
            'description': 'this is the description',
            'created': None,
        })
