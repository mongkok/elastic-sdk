import elastic_sdk
import pytest


@pytest.fixture(scope='module')
def client(request):
    return elastic_sdk.Client(index_name='test')
