# Database Persistence Guide for Dokploy Deployment

## Problem
When redeploying the app through Dokploy, the database was being deleted, causing data loss in production.

## Solution ✅
The database now persists across deployments using **Docker Named Volumes**.

---

## What Was Fixed

### 1. **Named Volume for PostgreSQL** (Already Working)
```yaml
volumes:
  - pgdata:/var/lib/postgresql/data/
```
This ensures all PostgreSQL data persists across container recreations.

### 2. **Added Health Checks**
```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U postgres"]
```
Ensures Django waits for the database to be fully ready before connecting.

### 3. **Added Restart Policies**
```yaml
restart: unless-stopped
```
Containers automatically restart if they crash, but can be manually stopped.

### 4. **Added Static and Media Volumes**
```yaml
volumes:
  - static_volume:/app/staticfiles
  - media_volume:/app/media
```
Preserves uploaded files and static assets across deployments.

---

## Important: Dokploy Configuration

### ⚠️ **CRITICAL - In Dokploy Dashboard:**

When deploying/redeploying in Dokploy, ensure:

1. **Never use "Clean Build" or "Remove Volumes"** - This deletes your database!
2. **Use normal "Deploy" or "Redeploy"** - This preserves volumes
3. **Check volume persistence settings** in Dokploy project settings

### To verify volumes are persisting (Optional):

If you want to check that volumes exist (not required for operation):

```bash
# SSH into your Contabo server
ssh your_user@your_server

# List Docker volumes
docker volume ls

# You should see:
# real_estate_broker_pgdata
# real_estate_broker_static_volume
# real_estate_broker_media_volume
```

**Note:** These volumes are created automatically by Docker Compose. This command is only for verification.

---

## How It Works

### Container vs Volume Storage

**BAD (Data Loss):**
```
Container → Database files inside container → 🔴 DELETED on redeploy
```

**GOOD (Data Persists):**
```
Container → Volume (external storage) → ✅ PERSISTS on redeploy
```

### Volumes are Stateful, Containers are Stateless
- **Containers**: Temporary, recreated on each deploy
- **Volumes**: Permanent storage, survive container recreations

---

## Database Backup Strategy

### 1. **Automated Backups** (Recommended)

Add this service to your `docker-compose.yml`:

```yaml
  db-backup:
    image: postgres:14
    depends_on:
      - db
    volumes:
      - ./backups:/backups
      - pgdata:/var/lib/postgresql/data:ro
    environment:
      PGPASSWORD: postgres
    entrypoint: |
      bash -c 'bash -s <<EOF
      trap "break;exit" SIGHUP SIGINT SIGTERM
      sleep 60s
      while /bin/true; do
        pg_dump -h db -U postgres -d postgres > /backups/backup_$$(date +%Y%m%d_%H%M%S).sql
        echo "$$(date +%Y-%m-%d_%H:%M:%S) - Backup created"
        ls -t /backups/*.sql | tail -n +8 | xargs rm -f
        sleep 86400
      done
      EOF'
    networks:
      - app_net
```

This creates daily backups and keeps the last 7 backups.

### 2. **Manual Backup Command**

```bash
# Backup
docker exec postgres_db pg_dump -U postgres postgres > backup_$(date +%Y%m%d).sql

# Restore
cat backup_20260109.sql | docker exec -i postgres_db psql -U postgres -d postgres
```

### 3. **Backup Before Major Changes**

Always backup before:
- Updating Django version
- Running complex migrations
- Major code changes

---

## Troubleshooting

### Problem: Database still gets deleted
**Solution**: Check Dokploy settings - don't use "Clean Build"

### Problem: "Database connection refused"
**Solution**: The database is starting. Wait 10-15 seconds and try again.

### Problem: Old data not appearing after redeploy
**Solution**: 
1. Check if the volume still exists: `docker volume ls`
2. If missing, restore from backup
3. Check Dokploy didn't remove volumes

### Problem: Need to reset database in production
```bash
# DON'T DO THIS IN PRODUCTION WITHOUT BACKUP!
docker-compose down -v  # ⚠️ This DELETES volumes!
docker-compose up -d
```

---

## Migration Best Practices

### Your entrypoint.sh already handles migrations correctly:
```bash
python manage.py migrate
```

This is **safe** because:
- ✅ Migrations are idempotent (can run multiple times safely)
- ✅ Django tracks which migrations have run
- ✅ Only new migrations are applied
- ✅ Existing data is not deleted

---

## Production Checklist

Before deploying to production:

- [x] Named volumes configured for database
- [x] Named volumes configured for media files
- [x] Named volumes configured for static files
- [x] Health checks enabled
- [x] Restart policies set
- [ ] Backup strategy implemented
- [ ] Backup restoration tested
- [ ] Monitor disk space on Contabo server
- [ ] Set up monitoring/alerts for database

---

## Additional Recommendations

### 1. **Add MEDIA_ROOT to Django settings**
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 2. **Update Dockerfile to create media directory**
```dockerfile
RUN mkdir -p /app/media /app/staticfiles
```

### 3. **Configure Nginx to serve media files**
In your nginx configuration, add:
```nginx
location /media/ {
    alias /app/media/;
}
```

### 4. **Monitor Volume Size**
```bash
# Check volume sizes
docker system df -v

# Clean up unused volumes (be careful!)
docker volume prune
```

---

## Questions?

If you still experience data loss:
1. Check Dokploy logs during deployment
2. Verify volumes exist: `docker volume ls`
3. Check volume mount points: `docker inspect <container_name>`
4. Ensure you're not using `docker-compose down -v` anywhere

---

**Remember**: Docker volumes are the correct solution for database persistence. Your current setup is now properly configured! 🎉
