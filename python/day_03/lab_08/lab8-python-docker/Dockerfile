FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install poetry

COPY . .

RUN poetry install


CMD ["poetry", "run", "python", "main.py"]
