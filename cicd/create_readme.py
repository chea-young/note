import requests

owner = 'chea-young'
repo = 'note'
url = f'https://api.github.com/repos/{owner}/{repo}/issues'



def get_issue(issue_num):
    response = requests.get(url+f'/{issue_num}')
    issue = response.json()

    return issue

issue = get_issue(2)