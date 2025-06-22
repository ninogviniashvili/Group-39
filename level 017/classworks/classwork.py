#1. while loop-ის მეშვეობით გამოიტანეთ ციფრები 0-დან 10-მდე.
#2. while loop-ის მეშვეობით გამოიტანეთ ციფრები 20-დან 10-მდე.
#3. while loop-ის მეშვეობით გამოიტანეთ 'goa' 5-ჯერ.
#4. მომხმარებელს შემოატანინეთ საიდუმლო სიტყვა და თუ ის დაემთხვა თქვენს საიდუმლო სიტყვას, 
# დაუპრინტეთ 'match'.

#1

i = 0

while i < 10 :
    print(i)
    i = i + 1


#2

i = 20

while i > 10:
    print(i)
    i = i - 1


#3

#...


#4

password = 13243546

password_guess = int(input("enter password: "))
password_guess = int(input("try again"))

print("match")