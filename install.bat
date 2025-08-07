@echo off
setlocal

REM Define the name of the native messaging host
set HOST_NAME=com.my_company.video_downloader

REM Get the full path to the manifest file in the same directory as this script
set MANIFEST_PATH=%~dp0native_host_manifest.json

echo Registering Native Messaging Host: %HOST_NAME%
echo Manifest path: %MANIFEST_PATH%

REM Register for Google Chrome
reg add "HKEY_CURRENT_USER\Software\Google\Chrome\NativeMessagingHosts\%HOST_NAME%" /ve /t REG_SZ /d "%MANIFEST_PATH%" /f > nul
if %errorlevel% equ 0 (
    echo Successfully registered for Google Chrome.
) else (
    echo ERROR: Failed to register for Google Chrome.
)

REM Register for Microsoft Edge
reg add "HKEY_CURRENT_USER\Software\Microsoft\Edge\NativeMessagingHosts\%HOST_NAME%" /ve /t REG_SZ /d "%MANIFEST_PATH%" /f > nul
if %errorlevel% equ 0 (
    echo Successfully registered for Microsoft Edge.
) else (
    echo ERROR: Failed to register for Microsoft Edge.
)

echo.
echo Registration complete. Press any key to exit.
pause > nul
endlocal
