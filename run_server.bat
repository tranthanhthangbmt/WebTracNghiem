@echo off
echo Dang khoi dong may chu cuc bo...
echo Vui long khong tat cua so nay khi dang su dung web.

:: Check if python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Khong tim thay Python. Vui long cai dat Python hoac su dung VS Code Live Server.
    pause
    exit /b
)

:: Start server in background
start "" http://localhost:8000
python -m http.server 8000
