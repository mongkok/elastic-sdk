Elastic SDK
===========

|Pypi| |Wheel| |Build Status| |Codecov| |Code Climate|


Python SDK for Elasticsearch


Installation
------------

Install from Pypi.

.. code:: sh

    pip install elastic-sdk


Quick start
-----------

**Client**

.. code:: python

    >>> import elastic_sdk
    >>> client = elastic_sdk.Client(index_name='defocus', hostnames=['elastic:9200'])

**Queries**

.. code:: python

    >>> client.q(user__username='me')


Tests
-----

.. code:: sh

    make test


.. |Pypi| image:: https://img.shields.io/pypi/v/elastic-sdk.svg
   :target: https://pypi.python.org/pypi/elastic-sdk

.. |Wheel| image:: https://img.shields.io/pypi/wheel/elastic-sdk.svg
   :target: https://pypi.python.org/pypi/elastic-sdk

.. |Build Status| image:: https://travis-ci.org/mongkok/elastic-sdk.svg?branch=master
   :target: https://travis-ci.org/mongkok/elastic-sdk

.. |Codecov| image:: https://img.shields.io/codecov/c/github/mongkok/elastic-sdk.svg
   :target: https://codecov.io/gh/mongkok/elastic-sdk

.. |Code Climate| image:: https://codeclimate.com/github/mongkok/elastic-sdk/badges/gpa.svg
   :target: https://codeclimate.com/github/mongkok/elastic-sdk
