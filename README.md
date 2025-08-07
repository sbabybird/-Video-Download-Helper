# Video Download Helper

A browser extension (Chrome/Edge) that detects videos on websites and uses a local `yt-dlp` instance to download them.

This project was collaboratively developed with Google's Gemini.

## Features

- **One-Click Downloads**: Adds a simple download button overlay on video players.
- **Broad Compatibility**: Works on many websites thanks to `yt-dlp`.
- **Site-Specific Adapters**: Includes enhanced support for:
  - YouTube (and other generic `<video>` sites)
  - Twitter / X.com (correctly finds tweet permalinks from the timeline)
  - Pornhub (bypasses click-blocking layers)
- **Proxy Support**: Easily configurable to use a proxy for `yt-dlp`.

## How It Works

The extension has two main parts:

1.  **Browser Extension**: The frontend, written in JavaScript. A `content_script.js` scans pages for videos and injects the download button. When clicked, it sends the video URL to a `background.js` script.
2.  **Native Messaging Host**: The backend, written in Python (`native_host.py`). The background script passes the URL to this host. The host then constructs and executes a `yt-dlp` command to download the video.

This architecture is necessary because browser extensions cannot directly run local programs for security reasons.

## Installation

**Prerequisites:**

- **Python**: Must be installed and accessible via the `python.exe` command in your system's PATH.
- **yt-dlp**: Must be installed and accessible via the `yt-dlp.exe` command in your system's PATH.

**Steps:**

1.  **Download/Clone**: Get all the files from this repository onto your local machine.

2.  **Load Extension & Get ID**:
    - Open Chrome/Edge and go to `chrome://extensions` or `edge://extensions`.
    - Enable **Developer mode**.
    - Click **"Load unpacked"** and select this project's folder.
    - The extension will load. Copy its **ID** (a long string of letters).

3.  **Configure Manifest**:
    - Open the `native_host_manifest.json` file.
    - Replace `PASTE_YOUR_EXTENSION_ID_HERE` with the ID you just copied. (If you followed the development process, this is already done).

4.  **Register Native Host**:
    - Right-click the `install.bat` file and select **"Run as administrator"**. This creates a registry key that tells the browser where to find the `native_host_manifest.json` file.

5.  **Reload & Test**:
    - Go back to the extensions page and click the **reload icon** for the Video Download Helper.
    - Go to a supported website, find a video, and click the ⬇️ button!

## Configuration

- **Download Path**: Videos are saved to your user's `Downloads` folder by default. You can change this in `native_host.py` by modifying the `download_path` variable.
- **Proxy**: To use a proxy, edit the `command` list in `native_host.py` to include your proxy settings, for example: `command = [ytdlp_path, "--proxy", "127.0.0.1:21882", url, ...]`
