# Използваме по-стабилен Python образ
FROM python:3.9-bullseye

# Смяна на Debian mirror за по-бързо сваляне на пакети
RUN sed -i 's|http://deb.debian.org/debian|http://ftp.de.debian.org/debian|g' /etc/apt/sources.list

# Инсталиране на системни пакети с retry и cleanup
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

# Настройка на работната директория
WORKDIR /app

# Копиране на зависимостите и инсталиране на Python пакети
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копиране на цялото приложение
COPY . .

# Добавяне на wait-for-it.sh с безопасно сваляне
RUN curl -fsSL -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh

# Настройки на средата
ENV PYTHONUNBUFFERED=1

# Порт за приложението
EXPOSE 8050

# CMD: изчакване на PostgreSQL, после миграции и стартиране на сървъра
CMD ["sh", "-c", "./wait-for-it.sh db:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8050"]
