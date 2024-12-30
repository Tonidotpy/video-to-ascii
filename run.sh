#!/usr/bin/bash

frames="$1"

# python main.py "$vid" 480 480
for file in "$frames"/*.txt; do
  cat "$file"
  read -r -t 0.04
  printf "\033[H"
done
