@echo off
rem Windows build entry point: build <target>  (run "build" alone to list targets)
rem Starts build.ps1 without changing PowerShell's execution policy.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build.ps1" %*
exit /b %ERRORLEVEL%
