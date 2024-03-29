#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(f'The value of X-Request-Id is: {x_request_id}')
