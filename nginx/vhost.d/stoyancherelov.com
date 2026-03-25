location /media/ {
    alias /app/media/;
    expires 30d;
    add_header Cache-Control "public";
}
