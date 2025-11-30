#!/bin/sh
# Скрипт за изчакване на базата преди стартиране на Django

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
except:
    exit(1)
END
do
  echo "Database not ready, retrying in 3 seconds..."
  sleep 3
done

echo "Database is ready, running migrations..."
python manage.py migrate

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8050
