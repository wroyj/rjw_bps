#!/bin/bash
source ./config.sh

INPUT_DIR="$BASE_DIR/input"
BACKUP_DIR="$BASE_DIR/backup"
STAGING_DIR="$BASE_DIR/staging"
AUDIT_FILE="$BASE_DIR/audit.json"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_TARGET="$BACKUP_DIR/$TIMESTAMP"

echo "[$(date)] Starting backup..."

rsync -av --delete "$INPUT_DIR/" "$BACKUP_TARGET/"

rm -rf "$STAGING_DIR"/*
cp -r "$BACKUP_TARGET/"* "$STAGING_DIR/"

if command -v jq > /dev/null; then
    TEMP_FILE=$(mktemp)
    jq --arg ts "$TIMESTAMP" --arg path "$BACKUP_TARGET"     '.runs += [{"timestamp": $ts, "backup_dir": $path}]' "$AUDIT_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$AUDIT_FILE"
else
    echo "⚠️ jq not found; skipping audit update."
fi

echo "✅ Backup complete: $BACKUP_TARGET"