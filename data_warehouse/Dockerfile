# arquivo: data_warehouse/Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y git libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app/dbt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Mantém o container vivo para podermos entrar nele e rodar os comandos do dbt
CMD ["tail", "-f", "/dev/null"]