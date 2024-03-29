#!/bin/bash
# This script sends a GET request to the provided URL and displays the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" {URL} | grep 200 >/dev/null && curl -s {URL}

