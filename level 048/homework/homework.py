# 1
def divide_numbers(a, b):
    if b != 0:
        print(a / b)
    else:
        print("you cant devide by 0!")

# 2
def greet(name):
    print(f"hello, {name}!")

# 3
def print_age(birth_year):
    current_year = 2025
    age = current_year - birth_year
    print("your age is", age)

# 4
def multiply_by_five(number):
    print(number * 5)
# 5 
def user_info():
    age = int(input("age: "))
    name = input("name: ")
    print(f"your name is {name}and you are {age} years old.")

# 6
def multiply_string_number(number_str):
    number = int(number_str)
    print(number * 5)

# 7
def three_numbers_operations(a, b, c):
    print("sum:", a + b + c)
    print("multiply:", a * b * c)
    print("devision:", a / b / c if b != 0 and c != 0 else "cant divide by 0")
    print("subtraction:", a - b - c)

# 8
def print_third_index_element(my_list):
    if len(my_list) >= 4:
        print(my_list[3])
    else:
        print("list too short")

# 9
def print_index_of_element(my_list, number):
    if number in my_list:
        print(f"number's {number} index is:", my_list.index(number))
    else:
        print(f"number {number} isnt in the list.")

# 10
def print_numbers_up_to(n):
    for i in range(n + 1):
        print(i)
