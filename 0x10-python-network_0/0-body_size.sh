#!/usr/bin/python3

import subprocess

def get_response_body_size(url):
    """
    Function to get the size of the body of the response from a given URL using curl.

    Args:
    url (str): The URL to send the request to.

    Returns:
    int: The size of the body of the response in bytes.
    """
    # Use subprocess to run the curl command and capture the output
    command = f"curl -sI {url} | grep -i Content-Length | awk '{{print $2}}'"
    output = subprocess.check_output(command, shell=True).decode().strip()

    # Convert the output to an integer
    size = int(output) if output.isdigit() else 0

    return size

# Test the function with a sample URL
url = "http://localhost:5000"
response_size = get_response_body_size(url)
print(f"Size of the response body from {url}: {response_size} bytes")
