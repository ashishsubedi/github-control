# github-control

Easy to use github setup

# How to use
### Updated for Windows and Linux (Should also work on MAC).
### Make sure git-bash and python are already installed and configured as well

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
5. For Linux, <code> export PATH=$PATH:/path/to/github-control/</code>. For more information (https://opensource.com/article/17/6/set-path-linux)

## Note: For linux, executable permission should be given for create_github.sh using <code> sudo chmod 711 create_github.sh </code>

## Note: You may need to restart cmd/terminal for this to work.

# Functionalities

### Automatically initialize repo
## Windows
1. Open cmd and type <code> create_github -n [NAME of REPO] -p [ABSOLUTE PATH TO CREATE NEW REPO] </code>.
## Linux
1. Open terminal and type <code> create_github.sh -n [NAME of REPO] -p [ABSOLUTE PATH TO CREATE NEW REPO] </code>.
### Donot put the working directory in the path
### If your path doesn't contain the directory, it will be created with Readme.md. If you have directory with existing codebase, it will update the github with all those codes and initialize repo as well. 
2. If you want to include description follow above code with <code> -d [DESCRIPTION] </code>.
3. To make repo private, add <code> -s </code> to the above command.

## Enjoy. Feel free to response incase of any problem.
