import os, requests

GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]

headers = {"Authorization": "token " + GITHUB_API_KEY}
url = "https://api.github.com/user/repos?per_page=100&type=owner"

response= requests.get(url, headers=headers)
repos = response.json()

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
