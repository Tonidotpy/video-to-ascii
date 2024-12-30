#!/usr/bin/bash

frames="$1"

# python main.py "$vid" 480 480
for file in "$frames"/*.txt; do
  cat "$file"
  read -t 0.03
  echo "\033c"
done
