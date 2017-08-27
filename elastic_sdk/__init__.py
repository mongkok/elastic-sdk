"""
captions-sdk
~~~~~~~~~~~~
Python SDK for Elasticsearch
:copyright: (c) 2017 mongkok
:license: MIT, see LICENSE for more details
"""

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search as DSLSearch
from elasticsearch_dsl.query import Q


__version__ = '0.0.1-dev'


class Search(DSLSearch):

    def all(self):
        return self[:self.count()]

    def hits(self):
        return super().execute().hits

    def q(self, **kwargs):
        return self.query(Q('match', **kwargs))

    def multi_match(self, q, fields, **kwargs):
        query = Q('multi_match', query=q, fields=fields, **kwargs)
        return self.query(query).highlight(*fields)

    def exists(self, field):
        return self.filter('exists', field=field)

    def idx(self, id, body, **kwargs):
        if self._doc_type:
            kwargs.setdefault('doc_type', self._doc_type[0])

        return self._using.index(
            index=self._index[0],
            id=id,
            body=body,
            **kwargs)


class Client(object):

    def __init__(self, index_name, hostnames=None, doc_prefix=None, **kwargs):
        self.index_name = index_name
        self.doc_prefix = doc_prefix

        if hostnames is None:
            hostnames = ['127.0.0.1:9200']

        self.es = Elasticsearch(hostnames, **kwargs)
        self.es.indices.create(index=self.index_name, ignore=400)

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            doc_type = self._get_doc_type(attr)
            return self.search(doc_type=doc_type)

    def _get_doc_type(self, doc_name):
        if self.doc_prefix is not None:
            return '{}.{}'.format(self.doc_prefix, doc_name)
        return doc_name

    def get(self, **kwargs):
        return self.es.get(index=self.index_name, **kwargs)['_source']

    def delete(self, doc_name, id):
        doc_type = self._get_doc_type(doc_name)
        return self.es.delete(index=self.index_name, doc_type=doc_type, id=id)

    def search(self, **kwargs):
        return Search(using=self.es, index=self.index_name, **kwargs)
