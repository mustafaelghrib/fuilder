FROM --platform=linux/amd64 python:3.11-slim AS builder

ARG ENVIRONMENT

ENV \
ENVIRONMENT=${ENVIRONMENT} \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
PYTHONFAULTHANDLER=1 \
PYTHONHASHSEED=random \
PIP_NO_CACHE_DIR=off \
PIP_DISABLE_PIP_VERSION_CHECK=on \
PIP_DEFAULT_TIMEOUT=100 \
POETRY_VERSION=1.4.1

COPY pyproject.toml /pyproject.toml

RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.create false && \
    poetry install $(if [ $ENVIRONMENT = 'production' ]; then echo '--only main'; fi) --no-interaction --no-ansi && \
    apt-get -y remove libpq-dev gcc && \
    apt-get -y autoremove && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

FROM --platform=linux/amd64 python:3.11-slim AS main

COPY --from=builder /opt/venv /opt/venv

WORKDIR /backend
COPY . .
