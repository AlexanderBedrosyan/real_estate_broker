#!/bin/bash

# PostgreSQL Restore Script
# Usage: ./restore_db.sh backup_20260109_120000.sql.gz

set -e

# Configuration
DB_CONTAINER="postgres_db"
DB_NAME="postgres"
DB_USER="postgres"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🔄 PostgreSQL Restore Script"
echo "================================"

# Check if backup file is provided
if [ -z "$1" ]; then
    echo -e "${RED}❌ Error: No backup file specified${NC}"
    echo "Usage: ./restore_db.sh <backup_file>"
    echo ""
    echo "Available backups:"
    ls -lh ./backups/backup_*.sql.gz 2>/dev/null || echo "No backups found"
    exit 1
fi

BACKUP_FILE=$1

# Check if backup file exists
if [ ! -f "${BACKUP_FILE}" ]; then
    echo -e "${RED}❌ Error: Backup file not found: ${BACKUP_FILE}${NC}"
    exit 1
fi

# Check if container is running
if ! docker ps | grep -q ${DB_CONTAINER}; then
    echo -e "${RED}❌ Error: Container ${DB_CONTAINER} is not running${NC}"
    exit 1
fi

# Warning
echo -e "${YELLOW}⚠️  WARNING: This will replace the current database!${NC}"
echo "Backup file: ${BACKUP_FILE}"
echo ""
read -p "Are you sure you want to continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "❌ Restore cancelled"
    exit 0
fi

# Create a safety backup of current database
echo "📦 Creating safety backup of current database..."
SAFETY_BACKUP="./backups/safety_backup_$(date +%Y%m%d_%H%M%S).sql"
docker exec ${DB_CONTAINER} pg_dump -U ${DB_USER} ${DB_NAME} > ${SAFETY_BACKUP}
gzip ${SAFETY_BACKUP}
echo -e "${GREEN}✅ Safety backup created: ${SAFETY_BACKUP}.gz${NC}"

# Restore database
echo "🔄 Restoring database..."

if [[ ${BACKUP_FILE} == *.gz ]]; then
    # Decompress and restore
    gunzip -c ${BACKUP_FILE} | docker exec -i ${DB_CONTAINER} psql -U ${DB_USER} -d ${DB_NAME}
else
    # Restore directly
    cat ${BACKUP_FILE} | docker exec -i ${DB_CONTAINER} psql -U ${DB_USER} -d ${DB_NAME}
fi

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Database restored successfully!${NC}"
    echo "📁 From: ${BACKUP_FILE}"
    echo "💾 Safety backup: ${SAFETY_BACKUP}.gz (in case you need to rollback)"
else
    echo -e "${RED}❌ Restore failed!${NC}"
    echo "You can restore the safety backup using this command:"
    echo "gunzip -c ${SAFETY_BACKUP}.gz | docker exec -i ${DB_CONTAINER} psql -U ${DB_USER} -d ${DB_NAME}"
    exit 1
fi

echo ""
echo "✨ Done!"
