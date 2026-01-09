# Quick Reference - Database Persistence

## ✅ Your Database is NOW Safe!

The database **will persist** across deployments because it's stored in a Docker volume (`pgdata`).

---

## 🚨 IMPORTANT: In Dokploy

**❌ NEVER DO THIS:**
- Don't click "Clean Build"
- Don't use "Remove Volumes"
- Don't run `docker-compose down -v`

**✅ ALWAYS DO THIS:**
- Use normal "Deploy" or "Redeploy"
- Volumes will automatically persist

---

## 📦 Backup Your Database (Optional - When Needed)

**Note:** Backups are optional. Run these on your Contabo server only when you want to create/restore backups.

```bash
# SSH into your server
ssh your_user@your_contabo_server

# Go to your project directory
cd /path/to/your/project

# Make scripts executable (first time only)
chmod +x backup_db.sh restore_db.sh

# Create a backup
./backup_db.sh
```

Backups are saved in `./backups/` directory.

---

## 🔄 Restore Database

```bash
# List available backups
ls -lh ./backups/

# Restore from a backup
./restore_db.sh ./backups/backup_20260109_120000.sql.gz
```

---

## 🔍 Verify Volumes Exist (Optional)

If you want to verify volumes are working (not required):

```bash
# SSH into server and check
docker volume ls | grep pgdata

# Should show: real_estate_broker_pgdata
```

**Note:** This is just for verification - volumes are created automatically by Docker.

---

## 📚 Full Documentation

See [DATABASE_PERSISTENCE_GUIDE.md](DATABASE_PERSISTENCE_GUIDE.md) for complete details.

---

## What Changed?

1. ✅ Added `restart: unless-stopped` to services
2. ✅ Added health checks for database
3. ✅ Added volumes for static and media files
4. ✅ Created backup/restore scripts
5. ✅ Configured Django MEDIA_ROOT
6. ✅ Updated Dockerfile to create necessary directories
