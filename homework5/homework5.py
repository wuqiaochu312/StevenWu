'''
-- Homework 1 + 2 Review --

3.1
1. Git vs. GitHub
Git is a version control system that tracks changes in files.
GitHub is a website where you store and share Git repositories online.

2. Terminal vs. Command Line
The terminal is the program window where you type commands.
The command line is the text-based interface inside the terminal.

3. Local vs. Remote Repository
A local repository is the copy on your computer.
A remote repository is the online copy, such as the one on GitHub.

4. Version Control
Version control is a system that keeps track of changes to files over time.

5. Staging Area
The staging area is where files are placed before making a commit.

6. git add
git add moves changed files into the staging area.

7. git commit
git commit saves the staged changes as a snapshot with a message.

8. git push
git push uploads your local commits to the remote repository.

9. git status
git status shows changed, staged, and untracked files.

10. git pull
git pull downloads changes from the remote repository and merges them.

11. pwd
pwd prints the current working directory.

12. ls
ls lists files and folders in the current directory.

13. cd
cd changes the current directory.

14. nano
nano opens a file in the nano text editor.

15. touch
touch creates a new empty file.

16. mv
mv moves or renames a file or folder.

17. rm
rm removes a file.

18. cat
cat prints the contents of a file in the terminal.

3.2
1. pwd

2. ls

3. 
cd ../brianna_repo
git pull

4. 
mv homework.py ../judy_decal/homework/

5.
cd ../judy_decal/homework

6.
cat homework.py

7.
git add .
git commit -m "done with hw5"
git push origin main

8.
git pull origin main
git push origin main
This error means the remote repository has changes that are not on your
local computer yet, so you need to pull first, and then push again.

9.
cd ~/Recent
'''

# --  Homework 3 Review --
#4.1
def checkDataType(value):
    return type(value)

#4.2
def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# --  Loops --
#5
def sumWithLoop(num):
    sum = 0
    for items in num:
        sum += items
    return sum

# -- Homework 4 Review --
#6.1 Lists
def duplicateList(old_list):
    new_list = []
    for items in old_list:
        new_list.append(items)
        new_list.append(items)
    return new_list

#6.2 Debugging
def square(num):
    return num * num

# --7 Running Your Code--
print(sumWithLoop([1,3,5,7,9]))