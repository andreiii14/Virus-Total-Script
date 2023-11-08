#!/usr/bin/python

import sys
import hashlib
import json
from virus_total_apis import PublicApi as public_api

# Read files
def file_input(file_name):
    try:
        with open(file_name, "rb") as file:
            output = file.read()
            return output
    except FileNotFoundError:
        print("[-]File not found")
        sys.exit(1)
    except IOError:
        print("[-]Error reading the file")
        sys.exit(1)

# Check for valid number of arguments
n = len(sys.argv)
if n != 2:
    print("[-]Invalid Syntax")
    print("Syntax : ./virus_total.py <file_name>")
    sys.exit(1)

api_key = "<your_api_key_here>"

if api_key == "<your_api_key_here>":
    print("[-]Please provide your VirusTotal API key")
    sys.exit(1)

content = file_input(sys.argv[1])
md5_sum = hashlib.md5()
md5_sum.update(content)
digest = md5_sum.hexdigest()

vt = public_api(api_key)

try:
    response = vt.get_file_report(digest)
    if response['response_code'] == 0:
        print("File not found in VirusTotal's database")
    else:
        print(json.dumps(response, sort_keys=False, indent=4))
except Exception as e:
    print(f"[-]An error occurred: {e}")
    sys.exit(1)
