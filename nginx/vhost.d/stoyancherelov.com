# Block common attack paths
location ~* ^/(wp-admin|wp-login|xmlrpc|\.php|\.env|\.git|\.aws|admin\.php|shell) {
    deny all;
    return 444;
}

# Security headers
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

# Media files
location /media/ {
    alias /app/media/;
    expires 30d;
    add_header Cache-Control "public";
}
