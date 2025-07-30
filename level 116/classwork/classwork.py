# 1) გააკეთეთ 1 მაგალითი თითოეულ ტიპის error-ზე და კომენტარებით დაწერეთ როდის ეშვება კონკრეტული error

# SyntaxError
# ValueError
# IndexError
# TypeError
# ZeroDivisonError

# ValueError
# try:
#     int("abc")
# except ValueError:
#     print("ValueError was raised")

# # IndexError
# try:
#     my_list = [1, 2, 3]
#     print(my_list[10])
# except IndexError:
#     print("IndexError was raised")

# # TypeError
# try:
#     x = "Age: " + 25
# except TypeError:
#     print("TypeError was raised")

# # ZeroDivisionError
# try:
#     y = 5 / 0
# except ZeroDivisionError:
#     print("ZeroDivisionError was raised")


try:
    num = int(input("enterr num: "))
    result = 10 / num
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("only numbers are allowed")
else:
    print(result)
finally:
    print("end of program")
