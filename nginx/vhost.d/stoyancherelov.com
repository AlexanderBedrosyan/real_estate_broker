# Rate limiting zones
limit_req_zone $binary_remote_addr zone=general:10m rate=30r/m;
limit_req_zone $binary_remote_addr zone=strict:10m rate=5r/m;
limit_conn_zone $binary_remote_addr zone=addr:10m;

# Block common attack paths
location ~* ^/(wp-admin|wp-login|xmlrpc|\.php|\.env|\.git|\.aws|admin\.php|shell|config\.) {
    deny all;
    return 444;
}

# Apply rate limiting to all requests
limit_req zone=general burst=20 nodelay;
limit_conn addr 20;

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
