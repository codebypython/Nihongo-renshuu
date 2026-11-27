@echo off
chcp 65001 >nul
cd /d "%~dp0"
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_all.ps1" -Action web
set "EXIT_CODE=%ERRORLEVEL%"
if not "%EXIT_CODE%"=="0" (
    echo.
    echo [FAIL] Khong the khoi chay chuong trinh. Vui long xem thong bao phia tren.
    pause
)
exit /b %EXIT_CODE%
