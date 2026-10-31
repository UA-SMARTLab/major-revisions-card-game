#!/bin/sh
# Opens Major Revisions in your default web browser. Double-click this file in Finder.
here="$(cd "$(dirname "$0")" && pwd)"
app="$here/app/index.html"
if [ ! -f "$app" ]; then
  echo "Could not find app/index.html next to this file."
  exit 1
fi
open "$app"
