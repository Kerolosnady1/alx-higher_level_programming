#!/usr/bin/python3

url=$1
response=$(curl -sI $url | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "Size of the response body in bytes: $response"
