#1. შექმენი ცვლადი, სადაც შეინახავ სტრინგს, შემდეგ გამოიტანე იმ სტრინგის მეორე ასო.

book = "Little woman"
print(book[1])

#2. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.

num1 = 50
num2 = 40
print(num1 + num2)

#3. შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია 
# (ასევე კომენტარის სახით აღწერეთ რა არის კონკატენაცია).

#axali stringi romelic gvadzlevs wina oris sheertebul versias da axal sityvas

movie = "sun"
movie1 = "glasses"
print(movie + movie1)

#4. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით
# რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)
num1 = 60
num2 = 20

print(num1 / num2)

#aq float imito gamoaqvs rom gayofa erti xazit weria aq gayofa ori xazit ro eweros anu ese // mashin intejers gamoitanda

#5. გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი

#1) !=
50 != 20

#2) <=
50 <= 60

#3) >=
123 >= 110

#4) >
40 > 30

#5) <
60 < 89

#6) ==

30 == 30

#7. გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა 
# (სულ უნდა იყოს რვა, გაიხსენეთ ნასწავლიდან)



#8. შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი

#9. შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.

for i in range(10):
    print(i)
#10. შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.

list = [2, 40, 20, 30, 10]

for i in range(3):
    print(list)


#11. შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".

word = "hello"

for i in range(i):
     
    print()

word1 = "world"

print(word + word1)
#12. შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
i = 1
while  i > 10:
    print(i)
    i = i +1
#13. შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს 
# რიცხვებს 50დან 60მდე.

#while 

#14. შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან,
#  სანამ ჯამი არ გაუტოლდება 50-ს
i = 1
while 1 < 50:
    print(i + 1)
    print(i)