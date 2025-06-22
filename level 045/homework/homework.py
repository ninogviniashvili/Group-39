#1. დაპრინტეთ Hello world.

print("Hello world")

#2. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.

num1 = 34
num2 = 65
print(num1 + num2)

#3. შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია (ასევე კომენტარის სახით აღწერეთ რა არის concatenation).

word1 = "sun"
word2 = "light"

print(word1 + word2)
#concatenation is to add strings together.

#4. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა float-ი და რა ქვია ამ convert-ს (implicit or explicit).
number = 10
num = 2

print(number//num)
#float იმიტომ გამოიტანა რომ ერთი დახრილი ხაზი წერია და არა ორი, ერთი დახრილი ხაზი როდესაც წერია კომპიუტერი ზუსტ განაყოფს აჩვენებს ხოლო მაგალითად 5/2 = 2.5  და 5//2 იქნება 2

#5. გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი.
#1
num = 10
num1 = 10
print(num == num1)

#2
num1 = 6
num2 = 3
print(num1 != num2)

#3
num = 5
num1 = 3
print(num < num1)

#4
number= 4
num = 7
print(number < num)

#6. შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2).
a = 8
b = 1
c = 5
d = 3

print(a + b != c + d)

#7. გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია.
print(True and True)
print(False and True)
print(True and False)
print(False and False)

print(False or True)
print(True or False)
print(True or True)
print(False or False)
#8. შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი.

#1
a = 2
b = 5
c = 2
print(a == b and c > a) 

#2
a = 10
b = 6
print(a != b or b > 0)  

#3
x = 2
y = 5
print(x < y and x != 0) 

#4
x = 10
y = 5
z = 8
print(x > y and z < y) 

#5
x = 10
y = 5
z = 3
print(x > y or y > z) 

#9. შექმენით for loop-ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
for i in range(1, 11):
    print(i)

#10. შექმენით for loop-ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".

word = "Hello, World!"
for text in word:
    print(text)

#11. შექმენით while loop-ი 1-დან 10-მდე რიცხვების დასაბეჭდად.

i = 1
while i <= 10:
    print(i)
    i = i + 1

#12. შექმენით while loop-ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.

i = 1
while i < 51:
    print(i)
    i = i + 1

#13. შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა გამოითვალე ამ სიის საშუალო არითმეტიკული. test case: [1,3,4,5,2] | output: 3

def nums(numbers):
    return sum(numbers) / len(numbers)

numbers = [5, 6, 7, 8, 9]
average = nums(numbers)
print(average)

#14. შექმენით ფუნქცია რომელსაც გადაეცემა  რიცხვების სია,თქვენი მოვალეობააა შექმნათ ახალი სია და ამ ახალ სიაში გამოიტანოთ ყოველი რიცხვის კვადრატი 
#(append) და შემდეგ დააბრუნეთ ახალი სია.test case: [3,12,5,2,6] | output: [9,144,25,4,36]

numbers = [8, 32, 7, 0, 13]

num = []
for number in numbers:
    num.append(number * number)

print(num)

#15. გაიხსენეთ ყველა list-ის და string-ის მეთოდები და გამოიყენეთ თავისი მაგალითებით.

#1

list = [0, 1, 2]
list.append(3) 
print(list) 

#2

list = [0, 1, 2, 0, 9, 8]
list.insert(2, 7)
print(list) 

#3

list = [1, 2, 3, 6, 9, 7, ]
list.pop(2) 
print(list) 

#4

list = [1, 2, 3, 6, 9, 7, ]
print(len(list))

#5

drink ="water"
print(drink.capitalize())

#6
name = "nino"
print(name.upper())

#7

word = "PROGRAM"
print(word.lower())

#8

text = "hello world"
print(text.find("o"))
