import requests
import os
import sys

OWNER = os.getenv('OWNER')
REPO = os.getenv('REPO')
TOKEN = os.getenv('TOKEN')
url = f'https://api.github.com/repos/{OWNER}/{REPO}/issues'

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_issue(issue_num):
    response = requests.get(url+f'/{issue_num}')
    issue = response.json()

    return issue

def issue_to_markdown(issue):
    markdown = f"# {issue['title']}\n"
    markdown += f"{issue['body']}\n\n"
    markdown += f"**Status:** {issue['state']}\n"
    markdown += f"**Created at:** {issue['created_at']}\n"
    markdown += f"**Updated at:** {issue['updated_at']}\n"
    markdown += f"**URL:** {issue['html_url']}\n"
    markdown += '\n---\n'
    return markdown

def save_to_readme(issue_id, content):
    filename = f'{issue_id}.md'
    with open(filename, 'w') as f:
        f.write(content)
    return filename
    

def main(issue_no):
    issue = issue = get_issue(issue_no);
    print(issue)
    markdown = issue_to_markdown(issue);
    filename = save_to_readme(issue_no, markdown)
    print(filename)

if __name__ == '__main__':
    issue_no = sys.argv[1]
    main(issue_no)