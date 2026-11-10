FROM python:3.14.10-slim
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . .
RUN uv sync --frozen --no-dev

EXPOSE 8000
ENTRYPOINT ["uv", "run", "--no-sync", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
