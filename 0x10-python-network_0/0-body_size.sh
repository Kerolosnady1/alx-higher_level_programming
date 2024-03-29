#!/bin/bash

url=$1
response=$(curl -sI $url | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "Size of the body of the response in bytes: $response"
