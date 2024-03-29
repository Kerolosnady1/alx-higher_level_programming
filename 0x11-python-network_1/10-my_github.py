#!/usr/bin/python3

import requests
import sys

def get_github_id(username, password):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        print(f"GitHub User ID for {username}: {user_data['id']}")
    else:
        print("Failed to retrieve GitHub User ID. Please check your credentials.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        get_github_id(username, password)
    else:
        print("Please provide both username and personal access token as arguments.")
