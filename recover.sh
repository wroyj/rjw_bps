#!/bin/bash
source ./config.sh

BACKUP_DIR="$BASE_DIR/backup"
STAGING_DIR="$BASE_DIR/staging"

if [ -z "$1" ]; then
    echo "Available backups:"
    ls -1 "$BACKUP_DIR" | sort -r
    echo ""
    echo "Restoring latest backup..."
    BACKUP_TS=$(ls -1 "$BACKUP_DIR" | sort -r | head -n 1)
else
    BACKUP_TS="$1"
fi

BACKUP_PATH="$BACKUP_DIR/$BACKUP_TS"

if [ ! -d "$BACKUP_PATH" ]; then
    echo "Backup $BACKUP_PATH not found."
    exit 1
fi

rm -rf "$STAGING_DIR"/*
cp -r "$BACKUP_PATH/"* "$STAGING_DIR/"

echo "[$(date)] Recovered backup $BACKUP_TS to staging."