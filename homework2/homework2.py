# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a version control system that tracks changes to files and lets you make commits.
# Github is a website that hosts Git repositories online.
# Git Bash is a terminal program mainly on Windows.
# 2) What’s the difference between the terminal and the command line?
#Terminal is the app you tpye commands into.
#Command line is the text based interface inside the terminal where you enter commands
# 3) How does Windows PowerShell differ from Git Bash?
#Powershell is Window's shell with its own command language.
#Git Bash is a Bash-like shell that uses many Unix-style commands and is closer to macOS
# 4) What’s the difference between Anaconda, conda, and Python?
#Python is the programming language that runs the code
#conda is a package and environment manager.
#Anaconda is a distribution that bundles python and conda and many common data science packages.
# 5) What is VS Code? 
#VS code is a code editor where you write code, run terminal, use extensions, and debug programs.
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
#Jupyter notebook is a document with cells you run interactively in a browser.
#JupyterLab is a newer interface that supports multiple notebooks/files/tabs ini one workspace.
# 7) What does ~/ mean?
# it measn your home directory.
# 8) What’s the difference between an absolute path and a relative path?
# An absolute path starts from the root of the filesystem, while a relative path starts from your current directory.
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
#Absolute path: /Users/wuqiaochu/python_decal_sp26/course_assignments/homework2
#Relative path: ../course_assignments/homework2
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..
# 11) What would rm ./ do in your current directory? (Don’t try it!)
# it will remove the current directory 
# 12) What do the following commands do?
# git add: adds fille contents to the staging area
# git commit: saves a snapshot of staged changes with a message.
# git push: uploads your commits to a remote repository

# 13) What's the difference between "git add ." and "git add <file>"?
# git add . will stage changes for all files in the current directory
# git add <file> will stage changes only for the specific file.
# 14) What do "git status" and "git log -1" do?
# git status shows which files are modified or staged or untracked and the current branch
# git log -1 shows the most recent commit and its message
# 15) What’s the difference between cloning a repository and pulling from it?
# git clone makes a new local copy of a remote repository.
# git pull updates an existing local repository by downloading the changes from the remote.
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# My frustrating error comes from running the code in python. Initally, I didn't know whether I was in the terminal or I was
# in the python running environment. Sometimes I use the shortcut on keyboard, and then it takes me to the python environment to run the code.
# After, when I clike on the run icon on the top right, an error occur and I don't know why. I fix this error when I learn lecture 2 (or 1) where I know
# I have to first use quit() exit the python.
# 17) What’s a question you still have? What’s something you’re confused about?
# None. Still looking for one. The lecture slides are so detailed !
# 18) Tell me a fun fact!
# disposable gloves are not oil-resistant
# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print( 1/2 * (3 * 4)) # it calculates the area of a triangle with base = 3 and height = 4