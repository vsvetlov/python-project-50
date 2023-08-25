install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

selfcheck:
	poetry check

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck test lint

.PHONY: install test lint selfcheck check build