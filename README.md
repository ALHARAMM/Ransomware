# Ransomware

This repository contains two Python scripts for file encryption and decryption using the cryptography library. They are designed for educational purposes. Please use them responsibly and ensure you have permission to encrypt or decrypt any files.

## Overview
The Ransomware Script provide a straightforward way to securely encrypt and decrypt files using advanced cryptographic techniques. This repository contains two main scripts:

encrypter.py: This script scans specified directories (excluding the C:\ drive on Windows) for files to encrypt. It generates a unique encryption key, encrypts the files, and sends the key to a designated Discord webhook for safekeeping.

decrypter.py: This script allows users to decrypt previously encrypted files. It requires the encryption key, which must be entered at runtime. The script will then locate and decrypt the files in the /home directory.

These tools utilize the cryptography library for secure encryption, making them ideal for educational demonstrations and controlled use cases. Users should ensure they have proper permissions before encrypting or decrypting files.

## Requirements
`Python 3.x
cryptography library
requests library
`
To install the required libraries, run:

`pip install cryptography requests`

## Configuration
Create a configuration file named config.conf in the same directory as the scripts. The file should contain:

`[settings]
webhook_url = YOUR_DISCORD_WEBHOOK_URL`

Replace YOUR_DISCORD_WEBHOOK_URL with your actual Discord webhook URL.

## Usage
# Encrypter Script
Open a terminal and navigate to the directory containing encrypter.py.

Run the script:
`python3 encrypter.py`
The script will encrypt files found in the specified directories and send the generated key to the Discord webhook.

# Decrypter Script
Open a terminal and navigate to the directory containing decrypter.py.

Run the script and provide the encryption key when prompted:

`python3 decrypter.py`
The script will decrypt all encrypted files found in the /home directory.

## Important Notes
Ensure you have the proper permissions to encrypt or decrypt files.
Keep the encryption key secure; without it, you cannot decrypt the files.
Use these scripts only in a controlled environment or for educational purposes.

## Acknowledgments
This project uses the cryptography library for encryption. For more information, visit the cryptography documentation.

## Issues and Contributions
If you have questions or encounter issues, please open an issue in this repository. Contributions are welcome!
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **ALHARAMM** - [GitHub Profile](https://github.com/ALHARAMM)
  
Happy coding!
