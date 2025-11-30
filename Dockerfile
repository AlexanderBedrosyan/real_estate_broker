FROM python:3.12-slim

WORKDIR /app

# Копирай зависимостите и ги инсталирай
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирай кода и entrypoint
COPY . .

# Направи entrypoint изпълним
RUN chmod +x entrypoint.sh

EXPOSE 8050

# Използвай entrypoint
ENTRYPOINT ["./entrypoint.sh"]
