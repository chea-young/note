import requests

owner = 'chea-young'
repo = 'note'
TOKEN = ''
url = f'https://api.github.com/repos/{owner}/{repo}/issues'

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
    with open(f'{issue_id}.md', 'w') as f:
        f.write(content)

def main(issue_no):
    issue = issue = get_issue(issue_no);
    markdown = issue_to_markdown(issue);
    save_to_readme(issue_no, markdown)

if __name__ == '__main__':
    main(2)