

# -- 3 Lists --
list_favorite_foods = ["Pizza", "Sushi", "Hamburger", "Noodles", "Ice cream"]
'''
I encountered this error:
Traceback (most recent call last):
  File "/Users/wuqiaochu/python_decal_sp26/StevenWu/homework4/homework4.py", line 1, in <module>
    list_favorite_foods = [Pizza, Sushi, Hamburger, Noodles, Ice_cream]
NameError: name 'Pizza' is not defined
I forgot to use "" in each of my term, so I fixed it by adding the ""
'''

# 3.1
print(list_favorite_foods[1])
print(list_favorite_foods[-1])
list_favorite_foods.append("Sandwich")
list_favorite_foods[0] = "apple"
del list_favorite_foods[2]
print(len(list_favorite_foods))
for items in list_favorite_foods:
    print(items.upper())
new_list = list_favorite_foods[::len(list_favorite_foods)-1]
if list_favorite_foods.count("potato") == 0:
    print("No potato!")
else:
    print("A potato!")

#3.2
numbers = list(range(0,21))
def get_first_15(numbers):
    new_list = numbers[0:15]
    return new_list

def get_every_5th(lst):
    new_list = lst[::5]
    return new_list

def reverse_and_stride(lst):
    new_list = lst[::-1]
    new_list = new_list[::3]
    return new_list
'''
I inital wrote:
def reverse_and_stride(lst):
    new_list = lst[::-1]
    new_list = new_list[::3]
so I got a None for printing step3. It's because I forgot to
add a return in this method. Then, I fix it by adding the return in it.
'''

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

#3.3
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(nubmers):
    total = 0
    for row in numbers:
        for column in row:
            total += column
    return total

def create_5times5_list():
    new_list = [
        [],
        [],
        [],
        [],
        []
    ]
    for i in range(0,5):
        for j in range(5 * i + 1, 5 * i + 6):
            new_list[i].append(j)
    return new_list
'''
Traceback (most recent call last):
  File "/Users/wuqiaochu/python_decal_sp26/StevenWu/homework4/homework4.py", line 81, in <module>
    print(create_5times5_list())
  File "/Users/wuqiaochu/python_decal_sp26/StevenWu/homework4/homework4.py", line 78, in create_5times5_list
    new_list[i].append(j)
IndexError: list index out of range

I had this error, which comes from my original code:
def create_5times5_list():
    new_list = []
    for i in range(0,5):
        for j in range(5 * i + 1, 5 * i + 6):
            new_list[i].append(j)
    return new_list

The new_list I defined didn't have the first row yet, so when I accessed
the first row, it said list index out of range. I fixed it by defining every
row of the list with a empty [].
'''

print(create_5times5_list())

def replace_multiples_3(numbers):
    for i in range(0,5):
        for j in range(0,5):
            if numbers[i][j] % 3 == 0:
                numbers[i][j] = "?"
    return numbers

def add_all_except_question_mark(numbers):
    Total = 0
    for i in range(0,5):
        for j in range(0,5):
            if numbers[i][j] != "?":
                Total += numbers[i][j]
    return Total

# -- 4 Dictionaries --

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for names in ages:
    print(names, ages[names])

# -- 5 Runing Your code --
print(create_5times5_list())      
    














