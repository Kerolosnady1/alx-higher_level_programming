#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    body = response.read()
    print("- Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))

