# Usar a imagem oficial do Python
FROM python:3.11-slim


WORKDIR /app


RUN pip install poetry


COPY . .


RUN poetry install


CMD ["poetry", "run", "python", "commands.py"]
