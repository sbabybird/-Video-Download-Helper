@echo off
REM Change directory to the script's location to ensure relative paths work correctly.
cd /d "%~dp0"

REM Execute the Python installer script.
python.exe install.py