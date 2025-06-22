#Easy:
#1. for loop-ის გამოყენებით დაპრინტეთ 10-მდე რიცხვები.
#2. for loop-ის გამოყენებით დაპრინტეთ 20-მდე რიცხვები.
#3. for loop-ის გამოყენებით დაპრინტეთ 'GOA Best' 10-ჯერ.

#1
for i in range(10):
    print(i)

#2
for i in range(20):
    print(i)

#3
for i in range(10):
    print("GOA Best")



#Medium:
#4. Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, 
# შემდეგ for loop-ით კი დაპრინტეთ "hello (მომხმარებლის სახელი)" 5 ჯერ.
#5. for loop-ის გამოყენებით დაპრინტეთ 20-მდე რიცხვები, თითოეული გაყოფილი 2-ზე.
#6. for loop-ის გამოყენებით დაპრინტეთ 15-მდე რიცხვები, თითოეული გამრავლებული 2-ზე.

#4
name=input("your name")

for i in range(5):
    print("hello" + name)

#5
for i in range(20):
    print(i // 2)
 
#6
for i in range(15):
    print(i * 2)


#Extreme:
#7. for loop-ის გამოყენებით დაპრინტეთ 10-მდე რიცხვები, თითოეულის კვადრატი.

for i in range(10):
    print(i * 10)


#8. for loop-ის გამოყენებით დაპრინტეთ 10-მდე არსებული ყველა რიცხვის ჯამი, 
# ეს ჯამი უნდა შეინახოს for loop-ის გარეთ შექმნილ ცვლად sum-ში.

for i in range(10):
    print(i)
