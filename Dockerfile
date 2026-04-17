FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create directories for media and static files
RUN mkdir -p /app/media /app/staticfiles

# Fix Windows CRLF line endings and set permissions
RUN sed -i 's/\r$//' entrypoint.sh && chmod +x entrypoint.sh

EXPOSE 8050

ENTRYPOINT ["./entrypoint.sh"]
