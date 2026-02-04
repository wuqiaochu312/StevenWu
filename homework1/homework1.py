# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer

b = 1.5
print(b)
print(type(b)) # b is a float

c = 3j
print(c)
print(type(c)) # c is a complex number

d = "hello"
print(d)
print(type(d)) # d is a string

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict - distionary

g = (1, 2)
print(g)
print(type(g)) # g is a tuple - an odered, unchangeable collection

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list 

i = True
print(i)
print(type(i)) # i is a Boolean values

j = None
print(j)
print(type(j)) # j is an NoneType - represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list

l = str(14)
print(l)
print(type(l)) # l is a string

m = 1e4
print(m)
print(type(m)) # m is a float

'''
I find 9 different data types: integer,float,string,complex,list,
dist,tuple,NoneType,Boolean. d and l both are string; b and m both are float;
e,h,and k are all list. l is a string, because the str() makes the integer 14
into a string type. I choose the data type - range
'''
n = range(5)
print(n)
print(type(n)) # n is a range

# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not smaller than 9
print(bool("abc")) # True,  "abc" is not a empty string
print(bool(123)) # True, 123 is not zero
print(bool(["apple", "cherry", "banana"])) #True, the list is not empty
print(bool(True)) #True, the bool(True) will return True itself
print(bool(False)) #False, the bool(False) will return False itself
print(bool(0)) #False, the value in bool() is zero
print(bool("")) #False, there is a empty string in ""
print(bool(" ")) #True, there is a space in " "
print(bool(())) #False, empty tuple is false
print(bool([])) #False, empty list is false
print(bool({})) #False, empty dictionary is false
print(bool(True and False)) #False
print(bool(True and True)) #True
print(bool(False and False)) #False
print(bool(True or False)) #True
print(bool(True or True)) #True
print(bool(False or False)) #False
print(bool(not(False))) #True
print(bool(not(True))) #False

'''
The bool() usually return False when its empty for the corresponding
data type and return True for non-zero and non-empty values. The experssion
bool(" ") surpriced me because I thought it was empty too, but it actually return True.
'''

print(5 > 1) #True, 5 is greater than 1
print(3 > 7) #False, 5 is not greater than 7

# --- Operators ---
print(10 + 5) #15 + performs addition
print(10 - 5) #5 - performs subtraction
print(2 * 4) #8 * performs multiplication
print(6 / 3) #2.0 /performs division
print(5 % 2) #1 %performs Remainder
print(3 ** 2) #9 **performs exponentiation
print(15 // 2) #7 // performs division and discards the fractional part of the result

print(5 == 2) #Flase, 5 is not equal to 2
print(10 != 10) #Flase, 10 is equal to 10
print(2 < 5) # True, 2 is smaller than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, 5 is smaller than 6
print(1 >= 10) # False, 1 is smaller than 10

x = 5
x += 5 # this is equal to x = x + 5
print(x) 

x -= 4 # this is equal to x = x - 4
print(x)

x *= 3 # this is equal to x = 3 * x
print(x)

#the operator "and" only return True when both sides are True
print(True and True) #True
print(True and False) #False

#the operator "or"  return True when one side is True
print(False or True) #True
print(False or False) #False

#the operator "not" return the opposite
print(not False) #True
print(not True) #False

'''
More questions:
/ is the normal division which return a float, while // is the division
that only take the integer part. 
% is taking the remainder, while // takes the integer part after division.
I would use %, for example 5 % 4 gives me 1
The assignment operator gives the variable a new value by performing a arithmetic operator,
for exmaple x += 5 is equal to x = x + 5.
'''

# --- Strings ---

my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # prints the first letter of my_string
print(my_string[1]) # prints the second letter of my_string
print(my_string[2]) # prints the third letter of my_string
print(my_string[3]) # prints the fourth letter of my_string
print(my_string[4]) # prints the fifth letter of my_string
print(my_string[-1]) # prints the last letter of my_string
print(my_string[1:3]) # prints the second and third letter of my_string
print(my_string[0:5:2]) #prints hlo, the each step length of 2
print(len(my_string))
print(my_string + "goodbye") #prints hellogoodbye
print(7 * my_string) #prints: hellohellohellohellohellohellohello

'''
the term slicing means to take and return parts of the string that we want. 
the manipulations my_string[1:3] and my_string[0:5:2] are doing the slicing.
'''

name = "Oski"
print("Hello, my name is", name) #prints: Hello, my name is Oski

name = "Oski"
print(f"Hello, my name is {name}") #also prints: Hello, my name is Oski

''' 
the difference here is that the first sentence uses a comma to combine the
variable name with the sentence. The second sentence use the f-string and insert it
in the apostrophes.
'''

# ---  Terminal Commands ---

''' 
cd
Changes directories. 
Use it to move from one folder to another
Example: cd Desktop

ls
list files in the current directory
exampel: ls

ls -a
list all files including the hidden files
example: ls -a

mkdir
make a new directory
example: mkdir homework1

cat
print the contents of a file
example: cat homework1.py

pwd
print the current working directory
example: pwd

cd ..
goto the parent directory
example: cd ..

cd .
current directory
example: cd .

cd ~
go to your home directory
example: cd ~

cp
copy a file or folder
example: cp old.py new.py

mv
move or rename a file or folder
example: mv old.py new.py

rm
remove a file
example: rm old.py

clear
clear the termial screen
example: clear

grep
search for a pattern in a file
example: grep "hello" homework1.py
'''

''' 
Question:
3 other commands:

head
show the first lines of a flie
example: head -n 5 homework1.py

tail
show the last line of a file
example: tail -n 5 homework1.py

touch
create an empty file
example: touch notes.txt

ls -a will list all the files including the hidden files, but
ls doesn't include the hidden files. A hidden file is a file whose name
starts with a ".". Many hidden files store settings or configuration.

ls -l
long format listing 
including the permissions, owner, file size, and last modified time
example: ls -l homework1.py

grep -n
prints the line number next to each matching line
example: grep -n "hello" homework1.py 

cp -r
copy a folder recursively with all files inside
example: cp -r homework1 homework1_backup

'''