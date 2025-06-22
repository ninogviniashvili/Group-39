# 1. Write a function that takes three numbers and returns the largest one without using max().
# 2. Create a function that counts how many vowels are in a word, ignoring case.
# 3. Create a function that checks if a word is a palindrome. A palindrome is a word that reads the same forward and backward, like 'racecar' or 'level', ignoring capitalization.
# 4. Write a function that reverses a given string.


# 1

def largestfromall(a, b, c):
    largest = a  
    if b > largest:
        largest = b  
    if c > largest:
        largest = c  
    return largest

print(largestfromall(10, 25, 15))

# 2

def count(word):
    vowels = "aeiou"
    total = 0
    for i in word.lower():
        if i in vowels:
            total += 1
    return total

print(count("Hello"))
print(count("pretty"))
print(count("goodbye"))

# 3

brand = "prada"

if brand == brand[::-1]:
    print(f"{brand} is palindrome")
else:
    print(f"{brand} isn't palindrome")

# 4

def reverse(word):
    return word[::-1]
print(reverse("welcome"))
