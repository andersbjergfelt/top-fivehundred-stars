#!/usr/bin/env python3

import requests
from datetime import datetime
import json
repos = []
headers = {'Authorization': 'token ' + '#insert'}
language = "Python"
filename = f"{language}repos.json"
##print(f"creating file: '{filename}'")
for number in range(1, 6):
    results = requests.get(
    f'https://api.github.com/search/repositories?q=language:{language}&sort=stars&per_page=100&page={number}', headers=headers).json()
    try:
        for repo in results['items']:
            repo_name = repo['full_name']
            repo_lang = repo['language']
            repo_stars = repo['stargazers_count']
            repo_created = repo['created_at']

            print(
                f"Repository {repo_name}"
                f"Repository {repo_lang}"
                f"Repository {repo_stars}"
                f"Repository {repo_created}"
            )
            repos.append(
                {
                    "repo": repo_name,
                    "language": repo_lang,
                    "stars": repo_stars,
                    "created_at": repo_created
                }
            )
    except (Exception, KeyboardInterrupt) as e:
        print(f"Processing stopped because of '{results}'")
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(repos))
