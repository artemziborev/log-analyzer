.PHONY: lint test run coverage changelog

lint:
	black .
	isort .
	flake8 .
	mypy .

test:
	pytest --tb=short -q

run:
	python main.py --config config.yaml

coverage:
	poetry run coverage run -m pytest
	poetry run coverage report
	poetry run coverage html

changelog:
	poetry run cz changelog
