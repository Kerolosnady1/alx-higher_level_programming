#!/usr/bin/python3

import requests
import sys

def get_repository_info(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        repo_info = response.json()
        print(f"Repository Name: {repo_info['name']}")
        print(f"Owner: {repo_info['owner']['login']}")
        print(f"Description: {repo_info['description']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
    else:
        print("Repository not found.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        get_repository_info(repo_name, owner_name)
    else:
        print("Please provide the repository name and owner name as arguments.")
