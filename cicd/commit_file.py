import subprocess
import os

OWNER = os.getenv('OWNER')
REPO = os.getenv('REPO')
TOKEN = os.getenv('TOKEN')
url = f'https://api.github.com/repos/{OWNER}/{REPO}/issues'

def git_commit_and_push(issue_no, filename):
    try:
        subprocess.run(['git', 'add', filename], check=True)
        subprocess.run(['git', 'commit', '-m', f'Feature: update {filename} (#{issue_no})'], check=True)
        subprocess.run(['git', 'push'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'An error occurred while running git command: {e}')