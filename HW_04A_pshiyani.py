"""
SSW_567
Author: Priyankaben Shiyani
Project Description: Develop with the Perspective of the Tester in mind
"""
import json
import requests

def get_id_user():
    ''' Executed if GitHub username is invalid '''
    try:
        get = input("Enter GitHub ID:").lower()
        return get
    except ValueError:
        return " That was not valid input. Please try again."

def get_user_data(user_id):
    r = requests.get(f'https://api.github.com/users/{user_id}/repos')
    if '"message":"Not Found"' in r.text:
        return "The user ID does not exist"
    else:
        repository = {}
        res_json = json.loads(r.text)
        for repo in res_json:
            repository[repo['name']] = 0

        if len(repository.keys()) == 0:
            return "This user has no repository"
        else:
            """Returning a list of names of repositories of a GitHub account and number of commits for a repository"""
            for item in repository.keys():
                repository[item] = len(json.loads((requests.get(f'https://api.github.com/repos/'
                                                                f'{user_id}/{item}/commits')).text))
           
            for repo, commit_count in repository.items():
                print(f"Repo: {repo} Number of commits: {commit_count}")
        return repository
def main():
    """main function"""
    try:
        get_user_data(get_id_user())
    except ValueError:
        print('Bad data. Please try again.')
if __name__ == '__main__':
    main()
