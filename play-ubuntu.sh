#!/bin/sh
# Opens Major Revisions in your default web browser.
# In Files, right-click this file and choose "Run as a Program", or run ./play-ubuntu.sh in a terminal.
here="$(cd "$(dirname "$0")" && pwd)"
app="$here/app/index.html"
if [ ! -f "$app" ]; then
  echo "Could not find app/index.html next to this file."
  exit 1
fi
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$app"
elif command -v sensible-browser >/dev/null 2>&1; then
  sensible-browser "$app"
else
  echo "No browser opener found. Open this file in your browser: $app"
  exit 1
fi
