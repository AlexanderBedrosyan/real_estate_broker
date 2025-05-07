FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y gcc libpq-dev curl && \
    apt-get clean

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh

ENV PYTHONUNBUFFERED 1


EXPOSE 8050

CMD ["sh", "-c", "./wait-for-it.sh db:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8050"]

