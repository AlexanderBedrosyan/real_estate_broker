#!/bin/sh
# Скрипт за изчакване на базата преди стартиране на Django

echo "ENV debug:"
echo "DB_HOST=$DB_HOST"
echo "DB_PORT=$DB_PORT"
echo "DB_NAME=$DB_NAME"
echo "DB_USER=$DB_USER"
echo "DB_PASSWORD=$DB_PASSWORD"

echo "Waiting for database to be ready..."

while ! python - <<END
import psycopg2, os
try:
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=int(os.environ.get("DB_PORT", 5432)),
        database=os.environ.get("DB_NAME", "postgres"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres")
    )
    conn.close()
    exit(0)
except Exception as e:
    print("Database connection error:", e)
    exit(1)
END
do
  echo "Database not ready, retrying in 3 seconds..."
  sleep 3
done

echo "Database is ready, running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

python - <<END
import os
from django.contrib.auth import get_user_model
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_estate_broker.settings")

django.setup()
User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    if not User.objects.filter(username=username).exists():
        print("Superuser does not exist. Creating...")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created!")
    else:
        print("Superuser already exists. Skipping.")
else:
    print("Missing superuser environment variables. Skipping creation.")
END

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8050
