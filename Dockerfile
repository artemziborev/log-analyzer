FROM python:3.12-slim

ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . .

VOLUME ["/app/logs", "/app/reports", "/app/templates"]

CMD ["poetry", "run", "python", "main.py", "--config", "config.yaml"]
