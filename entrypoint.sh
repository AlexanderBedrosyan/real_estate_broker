#!/bin/sh
# Скрипт за изчакване на базата преди стартиране на Django

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
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
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
