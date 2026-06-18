import requests
import json
import base64
import os

cfg = json.load(open("config.json"))
api = cfg["repo_url"].replace("github.com", "api.github.com/repos")

def fetch_file(path="README.md"):
    url = f"{api}/contents/{path}"
    r = requests.get(url).json()

    if "content" in r:
        return base64.b64decode(r["content"]).decode()

    return ""

os.makedirs("output", exist_ok=True)

script = fetch_file()
open("output/script.txt", "w").write(script)

print("✓ Script extracted from GitHub → output/script.txt")
