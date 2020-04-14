from config import ACCESS_TOKEN
from github import Github
import os
import sys,argparse

g = Github(ACCESS_TOKEN)

def main():
    global g
    try:
        parser = argparse.ArgumentParser(description="Automatically Creates github repo in the path")
        parser.add_argument('-n','--name',help='Name of the repository',required=True)
        parser.add_argument('-d','--description',help='Description of the repository')
        parser.add_argument('-s','--private',help='Add this to make repo private',action='store_true')
        parser.add_argument('-p','--path',help="Root Path of the working folder",required=True)
        args = parser.parse_args()

        name,path,desc,private = args.name,args.path,args.description,args.private
        
        user = g.get_user()
        repo = user.create_repo(name,desc,private=private)
        if not os.path.exists(path):
            os.mkdir(path)
            with open(os.path.join(path,'Readme.md'),'w') as f:
                f.write("Created automatically using create-github")
        
        

        
        

        




    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()