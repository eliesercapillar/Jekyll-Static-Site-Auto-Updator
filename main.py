import sys
import os.path
from datetime import date, datetime
from git import Repo

# GitHub Pages will run a workflow to serve any changes to the site whenever a change is pushed to the correct branch.
# So all this script needs to do is
# - Open a .txt file
# - Read .txt file contents
# - Create a .md file containing the contents of the .txt
# - Modify the Front Matter at the top of the .md file
# - Save the new .md file in the correct repository directory.
# - Push the changes to GitHub.

# CLI arguments
# Files in the _posts folder must be saved in the following format: YYYY-MM-DD-name-of-file.md
txt_file_name = ""
save_path = "S:/Repositories/My-Development-Blog/_posts/"
#save_path = "./"
git_repo_path = "S:/Repositories/My-Development-Blog/.git"
commit_msg = "Automated post commit via Python Script."

# Constants

def process_cli_args():
    # CLI arguments are assumed to be in the order of
    # 1. a .txt file to be converted
    # 2. a save path (optional)

    print("Processing CLI arguments.\n")
    num_arguments = len(sys.argv)
    if num_arguments <= 1:
        print("No arguments provided.")
    elif num_arguments > 3:
        print("Too many arguments provided.")
    elif num_arguments >= 2:
        global txt_file_name, save_path
        txt_file_name = sys.argv[1]
        if num_arguments == 3:
            save_path = sys.argv[2]
    else:
        print("Not enough arguments provided.")

def parse_text():
    txt_file = open(txt_file_name, "r")
    contents = txt_file.readlines()
    txt_file.close()
    write_contents(contents)

def write_contents(contents):
    md_file_name = "-" + txt_file_name[:-4] # Truncate .txt
    md_file = create_file(md_file_name)

    # Write Front Matter
    md_file.write("---\n")
    md_file.write("layout: single\n")
    md_file.write(f"title: \"{contents[0][:-1]}\"\n")
    md_file.write(f"date: {str(date.today())} {datetime.now().strftime('%H:%M:%S')} -0600\n")
    md_file.write("categories: ex*periences\n")
    md_file.write(f"permalink: /:categories/{txt_file_name[:-4]}\n")
    md_file.write("---\n") 
    
    # Write contents
    # Skip the title and the empty line
    for line in contents[2:]:
        md_file.write(line)

    md_file.close()

def create_file(file_name):
    today = str(date.today())
    formatted_file_name = today + file_name + ".md"
    if os.path.exists(save_path):
        return open(os.path.join(save_path, formatted_file_name), "w")
    else:
        print(f"The path {save_path} does not exist. File was not made.\n")
        return None

def push_changes():
    print("Pushing changes to GitHub.\n")
    try:
        print("Getting Repo.\n")
        repo = Repo(git_repo_path)
        print("Getting git.\n")
        git = repo.git
        print("Changing branches\n")
        git.checkout('gh-pages')
        #print("Pulling recent from branch\n")
        #git.pull()
        print("Getting origin\n")
        origin = repo.remotes.origin
        print("Adding changes.\n")
        git.add('.')
        print("Committing changes.\n")
        git.commit('-m', commit_msg)
        print("Getting origin\n")
        #git.remote("rm", "origin")
        #git.remote("add", "origin", "https://github.com/eliesercapillar/My-Development-Blog.git")
        print("Pushing Changes.\n")
        git.push(origin, 'gh-pages')
        print("Successful push.\n")
    except Exception as error:
        print(f'Some error occured while pushing the code\nMessage is: {error}')


if __name__ == '__main__':
    process_cli_args()
    if (txt_file_name != ""):
        parse_text()
        push_changes()
    print("End of processing.\n")