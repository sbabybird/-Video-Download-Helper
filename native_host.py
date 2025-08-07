import sys
import json
import struct
import subprocess
import os
import logging

# --- Setup Logging ---
script_dir = os.path.dirname(os.path.realpath(__file__))
log_file_path = os.path.join(script_dir, 'native_host.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Native host started.")

# --- Configuration ---
ytdlp_path = 'yt-dlp.exe' # Use the command directly, relying on system PATH
download_path = os.path.expanduser('~/Downloads')

def get_message():
    try:
        raw_length = sys.stdin.buffer.read(4)
        if len(raw_length) == 0:
            logging.info("stdin closed, exiting.")
            sys.exit(0)
        message_length = struct.unpack('@I', raw_length)[0]
        message = sys.stdin.buffer.read(message_length).decode('utf-8')
        return json.loads(message)
    except Exception as e:
        logging.error(f"Error reading message: {e}")
        sys.exit(1)

# --- Main Loop ---
while True:
    try:
        message = get_message()
        logging.info(f"Received message: {message}")

        if message.get("url"):
            url = message["url"]
            
            output_template = os.path.join(download_path, '%(title)s.%(ext)s')
            command = [ytdlp_path, "--proxy", "127.0.0.1:21882", url, "-o", output_template]
            
            logging.info(f"Executing command: {' '.join(command)}")
            
            # Run the command in a new process
            subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
            logging.info("Subprocess started successfully.")

    except Exception as e:
        logging.error(f"FATAL: An unhandled exception occurred: {e}")
        sys.exit(1)