#!/bin/bash

# PostgreSQL Backup Script for Production
# Run this script regularly to backup your database

set -e

# Configuration
BACKUP_DIR="./backups"
DB_CONTAINER="postgres_db"
DB_NAME="postgres"
DB_USER="postgres"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup_${DATE}.sql"
KEEP_DAYS=7

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "🗄️  PostgreSQL Backup Script"
echo "================================"

# Create backup directory if it doesn't exist
mkdir -p ${BACKUP_DIR}

# Check if container is running
if ! docker ps | grep -q ${DB_CONTAINER}; then
    echo -e "${RED}❌ Error: Container ${DB_CONTAINER} is not running${NC}"
    exit 1
fi

# Create backup
echo "📦 Creating backup..."
docker exec ${DB_CONTAINER} pg_dump -U ${DB_USER} ${DB_NAME} > ${BACKUP_FILE}

if [ $? -eq 0 ]; then
    # Compress backup
    echo "🗜️  Compressing backup..."
    gzip ${BACKUP_FILE}
    BACKUP_FILE="${BACKUP_FILE}.gz"
    
    # Get file size
    SIZE=$(du -h ${BACKUP_FILE} | cut -f1)
    
    echo -e "${GREEN}✅ Backup created successfully!${NC}"
    echo "📁 File: ${BACKUP_FILE}"
    echo "📊 Size: ${SIZE}"
    
    # Remove old backups
    echo "🧹 Cleaning old backups (keeping last ${KEEP_DAYS} days)..."
    find ${BACKUP_DIR} -name "backup_*.sql.gz" -mtime +${KEEP_DAYS} -delete
    
    # List remaining backups
    echo ""
    echo "📋 Available backups:"
    ls -lh ${BACKUP_DIR}/backup_*.sql.gz 2>/dev/null || echo "No backups found"
    
else
    echo -e "${RED}❌ Backup failed!${NC}"
    exit 1
fi

echo ""
echo "✨ Done!"
