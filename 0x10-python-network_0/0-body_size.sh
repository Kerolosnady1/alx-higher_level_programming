#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes
url=$1
response=$(curl -sI $url | grep -i Content-Length | awk '{print $2}')
echo "Size of the response body: $response bytes"

