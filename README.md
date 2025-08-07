# Video Download Helper

[中文说明](README.zh-CN.md)

A browser extension (for Chrome/Edge) that detects videos on websites and uses a local `yt-dlp` instance to download them.

## Features

- **One-Click Downloads**: Adds a simple download button overlay directly onto video players.
- **Broad Compatibility**: Works on any website that `yt-dlp` supports.
- **Site-Specific Adapters**: Includes enhanced support for tricky sites.
- **Automatic Cookie Support**: Securely uses your browser's cookies to allow `yt-dlp` to download videos from sites that require a login.

## Installation Guide

**Prerequisites:**

- **Python**: You must have Python installed and accessible from your system's PATH.
- **yt-dlp**: You must have `yt-dlp.exe` installed and accessible from your system's PATH.

**Installation Steps:**

1.  **Download Project**: Download all files from this repository to a permanent folder on your computer.

2.  **Load Extension & Get ID**:
    - Open your browser and go to `chrome://extensions` or `edge://extensions`.
    - Enable **Developer mode**.
    - Click **"Load unpacked"** and select the project folder.
    - The extension will load. **Copy its ID** (a long string of letters).

3.  **Configure Manifest**:
    - Open the `native_host_manifest.json` file.
    - Replace `PASTE_YOUR_EXTENSION_ID_HERE` with the ID you just copied.

4.  **Run Installer**:
    - Right-click `install.bat` and select **"Run as administrator"**.
    - This will register the host application with your browser.

5.  **Reload Extension**:
    - Go back to the extensions page and click the **reload icon** for the Video Download Helper.

Installation is complete! Enjoy.