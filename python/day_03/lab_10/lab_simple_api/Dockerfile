# Usar uma imagem oficial do Python
FROM python:3.11-slim

FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* ./

RUN pip install poetry


WORKDIR /app


COPY ./ app


RUN poetry install


CMD ["poetry", "run", "fastapi", "dev", "main.py"]
