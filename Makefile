
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  test        to run tests"
	@echo "  test-all    to run tests using tox"
	@echo "  release     to make a release"

test:
	@pytest tests

coverage:
	@pytest\
		--verbose\
		--cov elastic_sdk\
		--cov-config .coveragerc\
		--cov-report term\
		--cov-report xml\
		tests

test-all:
	@tox

release:
	@python setup.py sdist upload
	@python setup.py bdist_wheel upload

.PHONY: help test coverage test-all release
