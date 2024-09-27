# Ransomware

A simple file encryption tool that utilizes the `cryptography` library to encrypt files on Windows and Linux systems. This tool sends the encryption key to a specified Discord webhook.

## Features

- Encrypts all files in user directories (excludes specified files).
- Supports both Windows and Linux operating systems.
- Sends the encryption key to a Discord webhook for easy access.
- Utilizes threading for faster encryption of multiple files.

## Requirements

- Python 3.x
- `cryptography` library
- `requests` library

You can install the required libraries using pip:

`pip install cryptography requests`

## Configuration
Create a configuration file named config.conf in the same directory as the script with the following structure:

`[settings]
webhook_url = YOUR_DISCORD_WEBHOOK_URL
Replace YOUR_DISCORD_WEBHOOK_URL with your actual Discord webhook URL.`

## Usage
Clone this repository:

`git clone https://github.com/yourusername/ransomware.git
cd ransomware`
Install the required libraries as mentioned above.

Edit the config.conf file to include your Discord webhook URL.

Run the script:

`python3 encrypt.py`

Disclaimer
This tool is intended for educational purposes only. Ensure you have permission to encrypt files on any system you use this tool on. Misuse of this software can lead to loss of data and legal consequences.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **ALHARAMM** - [GitHub Profile](https://github.com/ALHARAMM)


