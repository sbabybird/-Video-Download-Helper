@echo off
REM Change directory to the script's location to ensure relative paths work correctly.
cd /d "%~dp0"

REM Execute the python script using the python interpreter.
python.exe native_host.py