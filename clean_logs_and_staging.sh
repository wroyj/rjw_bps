#!/bin/bash

echo "🧹 Cleaning logs and staging directories..."

# Define directories
LOG_DIR="data/logs"
STAGING_DIR="data/staging"

# Clean logs
if [ -d "$LOG_DIR" ]; then
    echo "🗑 Clearing logs in $LOG_DIR"
    rm -f "$LOG_DIR"/*.log
else
    echo "❌ Log directory not found: $LOG_DIR"
fi

# Clean staging
if [ -d "$STAGING_DIR" ]; then
    echo "🗑 Clearing staging files in $STAGING_DIR"
    rm -f "$STAGING_DIR"/*
else
    echo "❌ Staging directory not found: $STAGING_DIR"
fi

echo "✅ Cleanup complete."