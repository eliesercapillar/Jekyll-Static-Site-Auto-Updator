import sys
import os.path
from datetime import date

# GitHub Pages will run a workflow to serve any changes to the site whenever a change is pushed to the correct branch.
# So all this script needs to do is
# - Open a .txt file DONE
# - Read .txt file contents
# - Create a .md file containing the contents of the .txt
# - Modify the Front Matter at the top of the .md file
# - Save the new .md file in the correct repository directory. DONE
# - Push the changes to GitHub.

# CLI arguments
txt_file_name = ""
#save_path = "S:/Repositories/My-Development-Blog/_posts"
save_path = "./"
# Files in the _posts folder must be saved in the following format: YYYY-MM-DD-name-of-file.md

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

    lines = txt_file.readlines()
    write_contents(lines)

    txt_file.close()

def write_contents(contents):
    md_file = create_file("-test")
    
    for line in contents:
        md_file.write(line)

    md_file.close()

def create_file(file_name):
    today = str(date.today())
    formatted_file_name = today + file_name + ".md"
    if os.path.exists(save_path):
        return open(os.path.join(save_path, formatted_file_name), "w")
    else:
        print(f"The path {save_path} does not exist.\n")
        return None


def push_changes():
    print("Pushing changes to GitHub.\n")

if __name__ == '__main__':
    process_cli_args()
    if (txt_file_name != ""):
        parse_text()
        push_changes()
    print("End of processing.\n")