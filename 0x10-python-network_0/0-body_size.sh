#!/bin/bash

url=$1
response=$(curl -sI $url | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
