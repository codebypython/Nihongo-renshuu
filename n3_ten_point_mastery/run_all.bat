@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "ACTION=%~1"
if "%ACTION%"=="" set "ACTION=menu"
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_all.ps1" -Action "%ACTION%"
set "EXIT_CODE=%ERRORLEVEL%"
if "%~1"=="" if not "%EXIT_CODE%"=="0" pause
exit /b %EXIT_CODE%
