# VirusTotal File Checker

This is a Python script that uses the VirusTotal API to check whether a given file is malicious or not. The script calculates the MD5 hash of the file and queries the VirusTotal database for the file's report.

## Prerequisites

- Python 3.x
- The `virus_total_apis` Python module

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git

1. Install the required Python modules:
pip install virus_total_apis

1. Replace "<your_api_key_here>" with your actual VirusTotal API key in the virus_total.py script.

## Usage
Run the script with the following command:

./virus_total.py <file_name>

Replace <file_name> with the name of the file you want to check.

Improvements
This script has been improved to enhance its functionality and error handling in the following ways:

- Added improved error handling for file access and API request errors.
- Ensured secure handling of the VirusTotal API key.
- Included a check for the status of the API response to determine if the file was found in VirusTotal's database.
