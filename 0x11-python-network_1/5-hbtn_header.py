#!/usr/bin/python3

import requests
import sys

url = sys.argv[1]
response = requests.get(url)
request_id = response.headers.get('X-Request-Id')
print(f"X-Request-Id: {request_id}")
