@echo off
REM CMD entry point for Windows (double-click / cmd.exe).
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0deploy.ps1" %*
exit /b %ERRORLEVEL%
