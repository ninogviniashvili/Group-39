#Random Functions:
#1. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მის კვადრატს.
def number(num):
    return num * num

result = number(10)
print(result)

#2. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.
def numbers(num1,num2):
    return num1 + num2

result = numbers(53, 56)
print(result)

#3. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს ყველაზე პატარას.

def number(num):
    return min(num) 

list = [4, 6, 2, 7, 3]
print(number(list))  

#4. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და ამოწმებს, არის თუ არა ის დადებითი.
def number(num):
    if num > 0:
        return "Positive"
    else:
        return "Negative"


print(number(5))  
print(number(-3))  
print(number(0))   

#5. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს მათ ჯამს.

def number(num):
    return sum(num)

numbers = [1, 2, 3, 4, 5]
print(number(numbers))  
