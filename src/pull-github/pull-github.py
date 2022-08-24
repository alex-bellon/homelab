#! /bin/python3
import os, requests
from dotenv import load_dotenv

load_dotenv('.env')
GITHUB_KEY = os.getenv('GITHUB_KEY')

headers = {"Authorization": "token " + GITHUB_KEY}

for i in range(1, 100):
    url = "https://api.github.com/user/repos?per_page=100&type=owner&page=" + str(i) 
    
    response = requests.get(url, headers=headers)
    repos = response.json()
    
    if not repos: break
    
    for repo in repos:
        name = repo["name"]
        directory = "/home/alex/GitHub/" + name
        source = repo["ssh_url"]

        if os.path.exists(directory):
            print("Pulling " + directory)
            os.chdir(directory)
            os.system("git pull")
        else:
            print("Creating " + directory)
            os.chdir("/home/alex/GitHub/")
            os.system("git clone " + source)
