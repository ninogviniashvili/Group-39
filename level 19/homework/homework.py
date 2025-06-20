#Python:

#გამეორება:
#1. შეინახეთ სამი ქალაქის სახელი ცალკე ცვლადში და დაპრინტეთ ისინი.

name = "Georgia"
name1 = "Spain"
name2 = "France"

print(name)
print(name1)
print(name2)

#2. შეართეთ ორი სიტყვა (მაგ., სახელი და გვარი) და დაპრინტეთ სრული სახელი.

name = "nino"
surname = "gvin"

print(name + " " + surname)

#3. აიღეთ ორი რიცხვი და დაპრინტეთ მათი ჯამი, სხვაობა, ნამრავლი და განაყოფი.

num1 = 60
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 // num2)
print(num1 * num2)

#4. მიანიჭეთ ერთი ცვლადის მნიშვნელობა მეორეს და დაპრინტეთ ორივე ცვლადი, 
#რომ ნახოთ შედეგი.

a = 15
b = a
print("a:", a) 
print("b:", b)


#5. შემოატანინეთ მომხმარებელს მისი საყვარელი ფერი და დაპრინტეთ წინადადება, 
#რომელშიც ეწერება ეს ფერი.

color = input("enter your favorite color")

print(" i love" + color)

#6. შეინახეთ სტრინგი, მთელი რიცხვი და float სამ განსხვავებულ ცვლადში და დაპრინტეთ მათი ტიპები.

name = "nino"
age = 12
num = 14.6

print(type(name))
print(type(age))
print(type(num))

#7. აიღეთ float რიცხვი, გადააკეთეთ იგი მთელ რიცხვად და შემდეგ დაპრინტეთ როგორც
# ორიგინალური float, ასევე გადაყვანილი მთელი რიცხვად.

float_number = 16.69
int_number = int(float_number)
print("Original float:", float_number)
print("Converted to integer:", int_number)

##9. ორ რიცხვზე შეასრულეთ  არითმეტიკული მოქმედებები (შეკრება, გამოკლება, გამრავლება, გაყოფა)
# და შედეგები შეინახეთ ცვლადებში. შედეგების დაპრინტეთ.

num1 = 180
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 // num2)
print(num1 * num2)

#10. აიღეთ სამი სტრინგი და გააერთიანეთ ისინი ერთ წინადადებად. დაბეჭდეთ საბოლოო წინადადება.
   #აქ არის კიდევ 6 დავალება, რომლებიც ფოკუსირებულია შედარების ოპერატორებზე 
   #პირობითების გამოყენების გარეშე:

str1 = "Python"
str2 = "is"
str3 = "awesome!"
sentence = str1 + " " + str2 + " " + str3
print(sentence)

#11. შეინახეთ ორი რიცხვი ცალკეულ ცვლადებში და გამოიყენეთ შედარების ოპერატორები 
#(`<`, `>`, `<=`, `>=`, `==`, `!=`) შედარებისთვის. დაპრინტეთ თითოეული შედარების შედეგი.

num1 = 10
num2 = 20
print(num1 < num2)  # True
print(num1 > num2)  # False
print(num1 <= num2)  # True
print(num1 >= num2)  # False
print(num1 == num2)  # False
print(num1 != num2)  # True

#12. შექმენით ცვლადები ორი სხვადასხვა ასაკისათვის. გამოიყენეთ შედარების ოპერატორები იმის 
#შესამოწმებლად, არის თუ არა ერთი ასაკი მეორეზე დიდი ან მისი ტოლი. დაპრინტეთ შედეგი.

age1 = 25
age2 = 30
print(age1 > age2)  # False
print(age1 >= age2)  # False

#13. სამ ცვლადს მიანიჭეტ რიცხვითი მნიშვნელობები. გამოიყენეთ შედარების ოპერატორები, 
#რათა შეამოწმოთ არის თუ არა პირველი ცვლადი მეორეზე ნაკლები და თუ მეორე მესამეზე ნაკლები. 
#დაპრინტეთ შედეგები.

a = 5
b = 10
c = 15
print(a < b)  # True
print(b < c)  # True

#14. ცვლადში შეინახეთ ორი სხვადასხვა სტრინგი და შეადარეთ ისინი ტოლობის (`==`) და 
#უტოლობა (`!=`) ოპერატორების გამოყენებით. დაპრინტეთ ამ შედარების შედეგები.

name = "hello"
lastname = "world"
print(name == lastname) 
print(name != lastname)


#New:

#1. Write an if-else statement that prints "Good morning!" if the current hour is before 12, 
# and "Good afternoon!" if it is 12 or later.

curent_hour = 10
if curent_hour < 12:
    print("good morning")
else:
    print("good afternoon")

#2. Create an if-else statement to check if the temperature exceeds 30 degrees. If it does, print "It's hot outside!"; otherwise, print "It's not too hot."

temperature = 35
if temperature > 30:
    print("its hot outside")
else: 
    print("its not too hot outside") 

#3. Create an if-else statement to determine if a person is a teenager. If the age is less than 19 print "You are a teenager!"; otherwise, print "You are not a teenager."

age = 17
if age < 19:
    print("your teenager")
else:
    print("you're not teenager")
