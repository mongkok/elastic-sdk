import os
import re

from setuptools import find_packages, setup


def get_long_description():
    with open('README.rst', 'r') as f:
        return f.read()


def get_version(package):
    with open(os.path.join(package, '__init__.py')) as f:
        pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
        return re.search(pattern, f.read(), re.MULTILINE).group(1)


setup(
    name='elastic-sdk',
    version=get_version('elastic_sdk'),
    license='MIT',
    description='Python SDK for Elasticsearch',
    long_description=get_long_description(),
    author='mongkok',
    author_email='dani.pyc@gmail.com',
    maintainer='mongkok',
    url='https://github.com/mongkok/elastic-sdk/',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'elasticsearch>=5.4.0',
        'elasticsearch-dsl>=5.3.0',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'elasticsearch>=5.4.0',
        'elasticsearch-dsl>=5.3.0',
        'pytest>=3.0.7',
        'responses>=0.5.1',
    ],
)
