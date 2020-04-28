# github-control

Easy to use github setup

# How to use

0. Clone or Download this repo
1. Download following python packages using cmd

- <code> pip install PyGithub </code>
- <code> pip install pygit2 </code>

2. Create new file called <code> config.py </code> and add the following:

- <code> ACCESS_TOKEN=<your_github_personal_access_token> </code>
- ## You can generate this token from your github accounts. Go to settings>developer settings> Personal Acccess Token
- Name whatever you want.
- # NOTE: Give user and repo access to the token

3. In create_github.bat file, update your python.exe location
4. Go to windows environment variables and add new user or system path pointing to this downloaded repo location (https://docs.alfresco.com/4.2/tasks/fot-addpath.html)

## Note: You may need to restart cmd for this to work.

# Functionalities

## Automatically initialize repo

1. Open cmd and type <code> create_github -n [NAME of REPO] -p [ABSOLUTE PATH TO CREATE NEW REPO] </code>.
2. If you want to include description follow above code with <code> -d [DESCRIPTION] </code>.
3. To make repo private, add <code> -s </code> to the above command.

## Enjoy. Feel free to response incase of any problem.
