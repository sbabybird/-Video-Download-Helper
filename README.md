# Video Download Helper

[中文说明](README.zh-CN.md)

A browser extension (for Chrome/Edge) that detects videos on websites and uses a local `yt-dlp` instance to download them.

## Features

- **Transparent Command-Line Interface**: A command prompt window pops up for every download, showing the live output from `yt-dlp`.
- **One-Click Downloads**: Adds a simple download button overlay directly onto video players.
- **Broad Compatibility**: Works on any website that `yt-dlp` supports.
- **Site-Specific Adapters**: Includes enhanced support for tricky sites.
- **Automatic Cookie Support**: Securely uses your browser's cookies to allow `yt-dlp` to download videos from sites that require a login.
- **User-Friendly Installation**: A simple installer (`install.bat`) handles all technical setup automatically.

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

3.  **Run Installer**:
    - Simply double-click the `install.bat` file.
    - A terminal window will open. **Paste the Extension ID** when prompted and press Enter.
    - The script will automatically create the configuration and register the host.

4.  **Reload Extension**:
    - Go back to the extensions page and click the **reload icon** for the Video Download Helper.

Installation is complete! Enjoy.
