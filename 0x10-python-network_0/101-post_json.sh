#!/bin/bash
# This script sends a JSON POST request to a specified URL and displays the response body
curl -s -X POST $1 -H "Content-Type: application/json" --data @${2}

