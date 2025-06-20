
#1. შექმენი ფუნცია, სადაც არგუმენტად გადასცემ ორ რიცხვს, შემდეგ დაპრინტე ამ ორი რიიცხვის განაყოფი.
def numbers(num1, num2) :
    print(num1 // num2)
numbers(40,8)

##2. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ სახელს, შემდეგ დაპრინტე მისალმების მესიჯი, სადაც ამ სახელს გამოიყენებ.
def name(name):
    print("hello" + "  " + name)
name("nino")
#3. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ დაბადების თარიღს, შემდეგ დაპრინტე თუ რამდენი წლისაა მომხმარებელი.
def calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    age = current_year - birth_year
    age -= (current_month, current_day) < (birth_month, birth_day)
    print(age)


calculate_age(1999 , 1 , 24, 2024, 10, 11)  


#4. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ რიცხვ, შემდეგ დაპრინტე ეს რიცხვი გამრავლებული 5-ზე.
def number(number1) :
    print(number1 * 5)
number(20)
#5. შექმენი ფუნქცია, სადაც პირველ არგუმენტად input()-ის გამოყენებით გადასცემ ასაკს, მეორე არგუმენტად კი input()-ის გამოყენებით გადასცემ სახელს, შემდეგ დაპრინტე, თუ რა ქვია მომხმარებელს და რამდენი წლის არის ის.
def user_info():
    age = input("please enter your age: ")
    name = input("please enter your age: ")
    print(name + " is " + age + " old.")

user_info()
