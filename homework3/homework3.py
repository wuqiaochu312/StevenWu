# 3 --Print Functions--
#3.1
def say_goodbye(name):
    print("Goodbye", name)

#3.2
def calculate_area_circle(radius):
    print(3.14 * radius ** 2)


# 4 --Return Functions--
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# 5 --Conditionals--
#5.1
def range_of_today_temperature(readings):
    Min = min(readings)
    Max = max(readings)
    return (Min,Max)

readings = [15, 14, 17, 20, 23, 28, 20]
#print(range_of_today_temperature(readings))

#5.2
def is_weekend(week_number):
    if week_number == 6 or week_number == 7:
        return True
    else:
        return False

#5.3
def calculate_fuel_efficiency(distance,fuel):
    return distance / fuel

#5.4
def last_digit_to_front(num):
    last_digit = num % 10
    other_digit = num // 10
    count = 0
    digit_for_count = other_digit
    while digit_for_count > 0:
        count += 1
        digit_for_count = digit_for_count // 10
    
    return last_digit * 10 ** count + other_digit

#print(last_digit_to_front(12345))

# 6 --Loops--
#6.1
def power(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result

#print(power(10,6))

#6.2
def find_max_and_min_for(list):
    Max = list[0]
    Min = list[0]
    for i in list:
        if i > Max:
            Max = i
        if i < Min:
            Min = i
    return (Min,Max)

#print(find_max_and_min_for([75,2,3,4,5,56,234,84]))


def find_max_and_min_while(list):
    Max = list[0]
    Min = list[0]
    i = 0
    while i < len(list):
        if list[i] > Max:
            Max = list[i]
        if list[i] < Min:
            Min = list[i]
        i += 1
    return (Min,Max)

#print(find_max_and_min_while([75,2,3,4,5,56,234,84]))

#6.3
def add_digit(num):
    result = 0
    while num > 0:
        result = result + num % 10
        num = num // 10
    return result

#print(add_digit(2468))
    
#7.1
list = [1,23,24,657,34,6438,-235,-2347]
print(find_max_and_min_for(list))
