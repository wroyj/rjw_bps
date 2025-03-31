#!/bin/bash

BACKUP_BASE="data/backup"
STAGING_DIR="data/staging"
LOG_FILE="data/logs/recover.log"

LATEST_BACKUP=$(ls -dt "$BACKUP_BASE"/*/ | head -n1)

if [ -z "$LATEST_BACKUP" ]; then
    echo "❌ No backup found." | tee -a "$LOG_FILE"
    exit 1
fi

echo "[🕓 $(date '+%Y-%m-%d %H:%M:%S')] Restoring from backup: $LATEST_BACKUP" | tee -a "$LOG_FILE"
cp "$LATEST_BACKUP"/*.csv "$STAGING_DIR/" 2>/dev/null
echo "[🕓 $(date '+%Y-%m-%d %H:%M:%S')] Recovery complete." >> "$LOG_FILE"