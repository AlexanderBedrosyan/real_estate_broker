FROM python:3.12-slim

WORKDIR /app

# Копирай зависимостите и ги инсталирай
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирай останалия код
COPY . .

EXPOSE 8050

# CMD остава за стартиране, ако не се използва command в compose
CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]
