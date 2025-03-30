#!/bin/bash

INPUT_FILE="data/staging/bp_data.csv"
DEST_FILE="data/input/bp_data.csv"

if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ No file found in staging to promote."
    exit 1
fi

cp "$INPUT_FILE" "$DEST_FILE"
echo "✅ Promoted: $INPUT_FILE -> $DEST_FILE"