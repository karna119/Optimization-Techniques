@echo off
REM Engineering Optimization Study Guide - Quick Start
REM This batch file starts the HTTP server and opens the application

echo.
echo ====================================================
echo   Engineering Optimization Study Guide
echo   Quick Start
echo ====================================================
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✓ Python found
echo ✓ Starting HTTP Server on http://localhost:8000
echo.
echo Study Guide Directory: %cd%
echo.
echo Press Ctrl+C in this window to stop the server
echo.

REM Start Python HTTP server
python -m http.server 8000

pause
