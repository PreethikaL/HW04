import requests
import json

def get_repo_details(username = 'PreethikaL'):
    repo_commit_result = []
    user_repos_api = 'https://api.github.com/users/{}/repos'.format(username)
    result = requests.get(user_repos_api)
    repos = json.loads(result.text)
    repo_commit_result.append('User : {}'.format(username))

    try:
        repos[0]['name']
    except(TypeError,KeyError,IndexError):
        return 'unable to fetch repository details from user'

    try:
        for repo in repos:
            repo_name=repo['name']
            commit_api = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo_name)
            commit_result = requests.get(commit_api)
            commit_json = json.loads(commit_result.text)
            repo_commit_result.append('{} Number of commits: {}'.format(repo_name, len(commit_json)))
            # print('{} Number of commits: {}'.format(repo_name, len(commit_json)))
    except(TypeError, KeyError, IndexError):
        return 'unable to fetch repository details from user'

    return repo_commit_result

if __name__ == '__main__':
    for repo_item in get_repo_details():
        print(repo_item)
