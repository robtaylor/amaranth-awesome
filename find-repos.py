#!/usr/bin/env python3
import json
import os
import re
import requests
import subprocess

from pathlib import Path

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel
from typing import Set


README_PATH = "README.md"
URL_PATTERN = r'\[.*?\]\((https?://[^\s)]+)\)'

API_KEY = os.environ['API_KEY']
if 'API_BASE' in os.environ:
    API_BASE = os.environ['API_BASE']
else:
    API_BASE = None
MODEL_ID = os.environ['MODEL_ID']

# Initialize the model configured in .env
model = LiteLLMModel(
    model_id=MODEL_ID,
    api_key=API_KEY,
    api_base=API_BASE,
    planning_interval=3
)

# Create CodeAgent instance
agent = CodeAgent(model=model, tools=[], add_base_tools=True,
                  additional_authorized_imports=['json'])


def extract_urls() -> Set[str]:
    with open(README_PATH, "r") as f:
        content = f.read()
    return set(re.findall(URL_PATTERN, content))

def find_git_repo(url):
    """Use smolagents and litellm to find git repository URL from content"""

    print(f"🔍 Searching for git repository URLs in {url} using smolagents...")

    load_dotenv()

    try:
        result = agent.run(f"Analyze the content at url and find any git repository URLs: {url}. Reply with a json formatted list of urls.")
        print(result)
        urls = re.findall(URL_PATTERN, result)

        return urls

    except Exception as e:
        print(f"❌ Error finding git repo: {e}")
        return None


def spider_url(url):
    """Spider a URL and return all found URLs as JSON"""
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        urls = set()

        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute
            absolute_url = urljoin(url, href)
            urls.add(absolute_url)

        return json.dumps(list(urls))

    except requests.exceptions.RequestException as e:
        print(f"❌ Error spidering {url}: {e}")
        return json.dumps([])


def validate_repo(url):
    print(f"🔍 Validating {url}...")
    try:
        print(f'running {["git", "ls-remote", url]}')
        subprocess.run(["git", "ls-remote", url], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"✅ {url} is a valid git repository")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ {url} is not a valid git repository")
        return False


def main():
    urls = extract_urls()
    repo_urls = []
    print(f"🔍 Found {len(urls)} repository URLs to check")

    def check_urls(urls, depth=0):
        if depth > 3:
            print("Git url not found")
        for url in sorted(urls):
            if validate_repo(url):
                repo_urls.append(url)
            else:
                found_urls = find_git_repo(url)
                if found_urls:
                    check_urls(found_urls, depth+1)

    check_urls(urls)
    print(f"🎉 Validation complete: {len(repo_urls)}/{len(urls)} URLs are valid git repositories")
    Path("repourls.json").write_text(json.dumps(repo_urls))
    print("🎉 Written `repourls.json`")


if __name__ == "__main__":
    main()
