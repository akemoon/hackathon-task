#!/bin/bash

# Paths to files
LOG1="/var/log/nginx/log1.log"
LOG2="/var/log/nginx/log2.log"
LOG3="/var/log/nginx/log3.log"
LOG4="/var/log/nginx/log4.log"

# Create files if they do not exist
touch "$LOG1" "$LOG2" "$LOG3" "$LOG4"

while true; do
    # Write logs
    tail -n 10 /var/log/nginx/my-access.log >> "$LOG1"
    
    # Check size of log1 (300 kilobytes = 307200 bytes)
    SIZE=$(stat -c%s "$LOG1")
    if [ "$SIZE" -gt 307200 ]; then
        LINES=$(wc -l < "$LOG1")  # Count rows from log1
        > "$LOG1"                 # Clean file
        echo "$(date '+%Y-%m-%d %H:%M:%S'): Cleared $LINES lines" >> "$LOG2"
    fi
    
    # Parse 5xx and 4xx from access.log
    awk '$9 ~ /^5[0-9][0-9]$/' /var/log/nginx/my-access.log >> "$LOG3"
    awk '$9 ~ /^4[0-9][0-9]$/' /var/log/nginx/my-access.log >> "$LOG4"
    
    sleep 5
done