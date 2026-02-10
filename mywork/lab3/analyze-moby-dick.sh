#!/usr/bin/env bash
SEARCH_PATTERN="$1"
OUTPUT="$2"
if [ -z "$OUTPUT" ]; then
  OUTPUT="results.txt"
fi
if [ -f "$OUTPUT" ]; then
  echo "Error: $OUTPUT already exists. Aborting."
  exit 1
fi
curl -s -o mobydick.txt https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
OCCURRENCES=$(grep -oi "$SEARCH_PATTERN" mobydick.txt | wc -l)
echo "The search pattern '$SEARCH_PATTERN' was found $OCCURRENCES time(s)." > "$OUTPUT"
grep -in "$SEARCH_PATTERN" mobydick.txt >> "$OUTPUT"

