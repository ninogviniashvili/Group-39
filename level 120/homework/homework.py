#1
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))

# 2
def concatenate_strings(*args):
    return ''.join(args)
print(concatenate_strings("Hello, ", "world", "!"))

# 3
def print_person_info(**kwargs):
    print(f"name: {kwargs.get('name')}, age: {kwargs.get('age')}")

# 4
def print_car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 5 
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("start function")
        result = func(*args, **kwargs)
        print("function ended")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()

# 6
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"ფუნქცია შესრულდა {end - start:.4f} წამში")
        return result
    return wrapper

@timer_decorator
def long_task():
    time.sleep(2)

long_task()

# 7
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))

# 8
def min_max(*args):
    return max(args), min(args)

print(min_max(3, 7, 1, 9, 4))

# 9

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_text():
    return "hello world"

print(say_text())


