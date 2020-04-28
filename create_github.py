from config import ACCESS_TOKEN
from github import Github
import pygit2
import os
import sys
import argparse
import base64
import time

g = Github(ACCESS_TOKEN)


def main():
    global g
    commit_msg = "Initial Commit"
    repo_exist = False

    parser = argparse.ArgumentParser(
        description="Automatically Creates github repo in the path")
    parser.add_argument(
        '-n', '--name', help='Name of the repository', required=True)
    parser.add_argument('-d', '--description',
                        help='Description of the repository')
    parser.add_argument(
        '-s', '--private', help='Add this to make repo private', action='store_true')
    parser.add_argument(
        '-p', '--path', help="Absolute Path of the working folder(if doesn't exit, creates it)", required=True)
    args = parser.parse_args()

    name, path, desc, private = args.name, args.path, args.description, args.private
    if desc == None:
        desc = ''
    repo_exist = True if(os.path.exists(path+'/'+name)) else False

    user = g.get_user()

    # repo = user.get_repo(name)
    repo = user.create_repo(name, desc, private=private)

    content_msg = "Created automatically using create-github"

    repo.create_file("Readme.md", commit_msg, content_msg)

    if(not repo_exist):
        credentials = pygit2.UserPass(user.email, ACCESS_TOKEN)
        callbacks = pygit2.RemoteCallbacks(credentials=credentials)
        repoClone = pygit2.clone_repository(
            repo.clone_url, os.path.join(path, repo.name), callbacks=callbacks)
        repoClone.remotes.set_push_url("origin", repo.clone_url)
    else:

        os.system(
            f'cd {os.path.join(path,name)} && echo {content_msg} > Readme.md')
        os.system(f'cd {os.path.join(path,name)} && git init')
        os.system(f'cd {os.path.join(path,name)} && git add .')
        os.system(
            f'cd {os.path.join(path,name)} && git commit -m "Added All files"')
        os.system(
            f'cd {os.path.join(path,name)} && git remote add origin {repo.clone_url}')
        os.system(
            f'cd {os.path.join(path,name)} && git push -f -u origin master')

    print('[SUCCESSFULLY CREATED REPO]')
    print(repo.clone_url)


if __name__ == '__main__':
    main()
