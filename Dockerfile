FROM python:3.11-slim
WORKDIR /app

ENV POETRY_VERSION=1.8.2
COPY poetry.lock pyproject.toml /app/
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi
COPY . .
