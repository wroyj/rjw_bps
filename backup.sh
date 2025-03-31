#!/bin/bash

BACKUP_DIR="data/backup/$(date '+%Y%m%d_%H%M%S')"
INPUT_DIR="data/input"
STAGING_DIR="data/staging"
LOG_FILE="data/logs/backup.log"

echo "[🕓 $(date '+%Y-%m-%d %H:%M:%S')] Starting backup..." >> "$LOG_FILE"

mkdir -p "$BACKUP_DIR"
rsync -av --progress "$INPUT_DIR/" "$BACKUP_DIR/" >> "$LOG_FILE" 2>&1

cp "$BACKUP_DIR"/*.csv "$STAGING_DIR/" 2>/dev/null

echo "[🕓 $(date '+%Y-%m-%d %H:%M:%S')] Backup complete: $BACKUP_DIR" >> "$LOG_FILE"