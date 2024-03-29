#!/bin/sh

echo "Usage: <program> <OUTPUT>"

INPUT="/dev/ttyACM0"
OUTPUT="$1"

while true; do
    cat "$INPUT" >> "$OUTPUT"
done