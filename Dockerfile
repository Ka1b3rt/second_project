FROM python:3.12-slim

ARG ENVIRONMENT="production"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    python3-dev \
    libpq-dev \
    build-essential \
    curl \
    git \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*


RUN pip install uv

WORKDIR /app

COPY ./src/ /app/src
COPY ./alembic/ /app/alembic
COPY pyproject.toml uv.lock alembic.ini /app/

RUN echo $ENVIRONMENT \
    && uv --version \
    && uv sync --frozen

RUN groupadd -r web && useradd -d /app -r -g web web \
    && chown web:web -R /app

USER web

WORKDIR /app/src
