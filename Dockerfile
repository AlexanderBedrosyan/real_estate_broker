# Python 3.9 Bullseye
FROM python:3.9-bullseye

# Оптимизираме Debian mirror
RUN sed -i 's|http://deb.debian.org/debian|http://ftp.de.debian.org/debian|g' /etc/apt/sources.list

# Системни пакети с retry и cleanup
RUN set -eux; \
    for i in 1 2 3 4 5; do \
        apt-get update && \
        apt-get install -y --no-install-recommends \
            gcc \
            libpq-dev \
            curl \
            ca-certificates && break || \
        (echo "Retrying apt-get install ($i)..."; sleep 10); \
    done; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# wait-for-it.sh
RUN curl -fsSL -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh

ENV PYTHONUNBUFFERED=1
EXPOSE 8050

# CMD използва .env за host и port
CMD ["sh", "-c", "./wait-for-it.sh $DB_HOST:$DB_PORT -t 60 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8050"]

