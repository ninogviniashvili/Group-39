# Python: 
# Easy:
# 1. შექმენით ცვლადი სახელად name, სადაც მომხმარებელს input-ის მეშვეობით შემოატანინებთ სახელს, 
# შემდეგ კი მისალმების მესიჯი, მაგალითად 'hello ' + (სახელი). 

name = input("Enter your name: ")
print("hello" + " " + name)  
# 2. შექმენით სამი ცვლადი, სამივეში შეინახეთ განსხვავებული ინფორმაციის ტიპები, შემდეგ კი დაპრინტეთ ისინი.
name="nino"
age=12
height = 1.65
print(name)
print(age)
print(height)
# 3. შექმენით ცვლადი სახელად user_name, სადაც მომხარებელს შემოატანინებთ სახელს, 
# შემდეგ შექმენით ცვლადი სახელად last_name, სადაც მომხმარებელს შემოატანინებთ გვარს, ბოლოს დაუპრინტეთ
#  მსგავსი მესიჯი: 'hello ' + (სახელი) + (გვარი).
user_name=input("Enter your name: ")
last_name=input("enter your last_name")
print("hello" + " " + user_name + " " + last_name)
 
# 4. კომენტარში ახსენით რა არის input და output, შემდეგ ახსენით რა არის კარგი პრაქტიკები და რომელი კარგი პრაქტიკები ვიცით.
#input - aris funqcia ris sashualebitac momxmarebels shemoaqvs monacemebi

# output - aris is rac gamodis kompiuteridan, rac shedegs abrunebs

# Hard:
# 5. შექმენით ორი ცვლადი, სადაც მომხმარებელს შემოატანინებთ ორ რიცხვს, შეასრულეთ ამ რიცხვებზე შეკრება, გამოკლება,
#  გამრავლება, გაყოფა და დაპრინტეთ შედეგები, (მინიშნება: input() მთლიანათ გადააქციეთ ინტეჯერად, int() 
# ფუნქციის მეშვეობით).
number1 = int(input("Enter first number: "))
number2 = int(input("enter second number: "))
print(number2 - number1)
print(number2 * number1)
print(number2 / number1)
print(number1  + number2) 