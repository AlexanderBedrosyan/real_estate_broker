FROM python:3.9-slim

# Install PostgreSQL client dev tools
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED 1

RUN python manage.py collectstatic --noinput

EXPOSE 8050

CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]
