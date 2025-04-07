.PHONY: format lint test ckech changelog

# Автоформатирование кода
format:
	poetry run black .
	poetry run isort .

# Проверка кода без изменений
lint:
	poetry run black --check .
	poetry run isort --check-only .
	poetry run flake8 .
	poetry run ruff .
	poetry run mypy src/app tests

# Запуск тестов с покрытием
test:
	poetry run coverage run -m pytest
	poetry run coverage report

# Быстрая проверка (линтинг + тесты)
check: lint test


changelog:
	poetry run cz changelog
