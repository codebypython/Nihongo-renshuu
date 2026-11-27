@echo off
setlocal
title Language Lab - JLPT N3 Sprint
if not exist "%~dp0he-thong\runtime\python.exe" (
    echo Hay giai nen toan bo tep ZIP truoc khi mo.
    pause
    exit /b 1
)
"%~dp0he-thong\runtime\python.exe" -B -X utf8 "%~dp0he-thong\runtime\launch.py" sprint %*
set "result=%ERRORLEVEL%"
if "%result%"=="130" exit /b 0
if "%result%"=="-1073741510" exit /b 0
if not "%result%"=="0" pause
exit /b %result%
