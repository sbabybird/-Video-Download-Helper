import sys
import os
import json
import winreg

def main():
    # --- Header ---
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================================")
    print("      Video Download Helper - Host Installer         ")
    print("=======================================================")
    print()

    # --- Instructions ---
    print("STEP 1: Load the extension in your browser")
    print("  1. Open chrome://extensions or edge://extensions.")
    print("  2. Enable Developer Mode.")
    print("  3. Click \"Load unpacked\" and select this project folder.")
    print()

    # --- User Input ---
    print("STEP 2: Enter the Extension ID")
    extension_id = input("--> Please enter the ID and press Enter: ")
    if not extension_id:
        print("\nERROR: No Extension ID provided. Installation cancelled.")
        input("Press Enter to exit.")
        sys.exit(1)

    # --- Configuration ---
    host_name = "com.my_company.video_downloader"
    script_dir = os.path.dirname(os.path.realpath(__file__))
    launcher_path = os.path.join(script_dir, "run_native_host.bat")
    manifest_path = os.path.join(script_dir, "native_host_manifest.json")

    manifest = {
        "name": host_name,
        "description": "Video Download Helper Host",
        "path": launcher_path,
        "type": "stdio",
        "allowed_origins": [
            f"chrome-extension://{extension_id}/"
        ]
    }

    # --- Generate Manifest ---
    print("\nSTEP 3: Generating configuration...")
    try:
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        print("  Success: Manifest file generated.")
    except Exception as e:
        print(f"  ERROR: Failed to create manifest file: {e}")
        input("Press Enter to exit.")
        sys.exit(1)

    # --- Register Host ---
    print("\nSTEP 4: Registering host with your browsers...")
    register_key(winreg.HKEY_CURRENT_USER, rf"Software\Google\Chrome\NativeMessagingHosts\{host_name}", manifest_path, "Google Chrome")
    register_key(winreg.HKEY_CURRENT_USER, rf"Software\Microsoft\Edge\NativeMessagingHosts\{host_name}", manifest_path, "Microsoft Edge")

    # --- Final Instructions ---
    print("\n=======================================================")
    print("      Installation Complete!                         ")
    print("=======================================================")
    print("\nIMPORTANT: Please go back to your browser and RELOAD the extension.")
    print()
    input("Press Enter to exit.")

def register_key(hive, key_path, manifest_path, browser_name):
    try:
        with winreg.CreateKey(hive, key_path) as key:
            winreg.SetValue(key, None, winreg.REG_SZ, manifest_path)
        print(f"  - Success: Registered for {browser_name}.")
    except Exception as e:
        print(f"  - ERROR: Failed to register for {browser_name}: {e}")

if __name__ == "__main__":
    main()
