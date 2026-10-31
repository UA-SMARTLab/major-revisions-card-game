@echo off
rem Opens Major Revisions in your default web browser. Double-click this file in File Explorer.
set "APP=%~dp0app\index.html"
if not exist "%APP%" (
  echo Could not find app\index.html next to this file.
  pause
  exit /b 1
)
start "" "%APP%"
