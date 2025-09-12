# 1 
def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return f"right age: {age}"

print(check_age(20))
print(check_age(-5))   

# 2

def check_word(word):
    if word == "":
        raise ValueError("word cannot be empty")
    return f"right word: {word}"

# 3

add_numbers = lambda a, b: a + b
print(add_numbers(3, 5))

# 4
c_to_f = lambda c: (c * 9/5) + 32

for c in [0, 10, 20, 30, 40]:
    print(c_to_f(c))

# 5 
nums = [3, 6, 9, 12, 15]
result = list(map(lambda x: x + 5, nums))
print(result)

# 6

words = ['hello', 'world', 'python']
result = list(map(lambda w: w.upper(), words))
print(result)

# 7 
nums = [5, 8, 11, 14, 17]
result = list(filter(lambda x: x > 10, nums))
print(result)

# 8
words = ['ant', 'elephant', 'dog', 'giraffe']
result = list(filter(lambda w: len(w) >= 5, words))
print(result)

# 9
nums = [2, 4, 6, 8]
result = list(map(lambda x: x * 2, nums))
print(result)

# 10
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x + 10, filter(lambda x: x % 2 == 0, nums)))
print(result)
