"""
SSW_567
Author: Priyankaben Shiyani
Project Description: Develop with the Perspective of the Tester in mind
"""

import requests

def get_id_user():
    ''' Executed if GitHub username is invalid '''
    try:
        get = input("Enter GitHub ID:").lower()
        return get
    except ValueError:
        return " That was not valid input. Please try again."

def get_data_user(get):
    ''' fetches user list of names of repositories of a GitHub account and 
        number of commits for a repository
     '''
    try:
        repost_url = f"https://api.github.com/users/{get}/repos"
        github_data_user = requests.get(repost_url).json() # fetches and converts to JSON
        di = dict()
        for item in github_data_user:
            commit_url = f"https://api.github.com/repos/{get}/{item}/commits"
            req = requests.get(commit_url).json() # fetches and converts to JSON
            di[item['name']] = len(req)
        return di
        
    except ValueError:
        print('Bad data.')

def main():
    """main function"""
    try:
        get_data_user(get_id_user())
    except ValueError:
        print('Bad data. Please try again.')

if __name__ == '__main__':
    main()