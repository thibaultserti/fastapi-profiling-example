ARG USER=appuser
ARG POETRY_VERSION=1.5.1

FROM python:3.10-slim
ARG USER
ARG POETRY_VERSION
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
# make sure all messages always reach console
    PYTHONUNBUFFERED=1

ENV UID=10001
LABEL org.opencontainers.image.description="fastapi-profiling-example"
RUN pip install poetry=="${POETRY_VERSION}" && \
    adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
# hadolint ignore=DL4006
RUN poetry export -f requirements.txt --without-hashes | pip install -r /dev/stdin
COPY src/app /app

EXPOSE 8080
USER ${USER}:${USER}
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
