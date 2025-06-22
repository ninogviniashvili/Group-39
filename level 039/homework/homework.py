#1. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ 5 რიცხვი და დაპრინტეთ ამ list-იდან მაქსიმალური რიცხვი.
list1 = [12, 33, 11, 5, 2.456,]
print(max(list1))

list2 = [11, 76, 36, 97, 0,]
print(max(list2))

list3 = [57, 79, 92, 124, 849,]
print(max(list3))

#2. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ 5 რიცხვი და დაპრინტეთ ამ list-იდან მინიმალური რიცხვი.
list1 = [12, 773, 11, 5, 2.456,]
print(min(list1))

list2 = [61, 76, 34, 17, 0,]
print(min(list2))

list3 = [77, 19, 52, 124, 844,]
print(min(list3))

#3. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ მინიმუმ 5 ელემენტი და დაპრინტეთ ამ list-ის სიგრძე.
list1 = [12, 33, 11, 5, 2.456, 385, 64, 15]
print(len(list1))

list2 = [11, 76, 36, 97, 46, 73, 71, 93]
print(len(list2))

list3 = [57, 79, 92, 124, 849, 65, 396, 29]
print(len(list3))

#4. შექმენით 3 სხვადასხვა list-ი, თითოში დაამატეთ 5 რიცხვი და დაპრინტეთ ამ list-იდან რიცხვების ჯამი.
list1 = [12, 33, 11, 5, 2.456,]
print(sum(list1))

list2 = [11, 76, 66, 97, 0,]
print(sum(list2))

list3 = [57, 79, 92, 184, 149,]
print(sum(list3))

#5. შექმენით 4 სხვადასხვა list-ი, თითოში დაამატეთ მინიმუმ 10 ელემენტი
#და დაპრინტეთ:
# 1) პირველ list-ის პირველიდან მეოთხე ელემენტამდე ცვლადები.
# 2) მეორე list-ის მეოთხედან მერვე ელემენტამდე ცვლადები ფორ ციკლის          გამოყენებით.
# 3) მესამე list-ის მეცხრედან მეექვსე ელემენტამდე ცვლადები გაითვალისწინეთ არა 6დან 9მდე არამედ 9დან 6მდე გამოიყენეთ უარყოფითი რიცხვები.
# 4) მეოთხე list-ში დაპრინტეთ მისი ყველა ცვლადი while ცოკლის გამოყენებით.

food = ["pasta", "lazania", "salad", "steak", "French fries", "Caesar salad", "Pizza", "Burger", "Sushi", "Tacos"]
print(food[0:3])

musicians = ["Lana Del Rey", "The Neighbourhood", "The Weeknd", "Michael Jackson", "Kanye West", "Travis Scott", "Playboi Carti", "Childish Gambino", "Frank Ocean", "Steve Lacy"]

#               -10                   -9               -8            -7                -6             -5                -4                 -3               -2           -1        
musicians = ["Lana Del Rey", "The Neighbourhood", "The Weeknd", "Michael Jackson", "Kanye West", "Travis Scott", "Playboi Carti", "Childish Gambino", "Frank Ocean", "Steve Lacy"]
print(musicians[-2:-5:-1]) 

food = ["pasta", "lazania", "salad", "steak", "French fries", "Caesar salad", "Pizza", "Burger", "Sushi", "Tacos"]

#(boss level);
#6. შექმენით def ფუნქცია რომელიც არგუმენტად აიღებს list-ს რომელშიც მომხმარებელი შეიყვანს მინიმუმ 5 რიცხვს და დაპრინტავს ამ list-ის 
# მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და list-ის სიგრძეს.

def list(numbers):
    max_number = max(numbers) 
    min_number = min(numbers)  
    total_sum = sum(numbers)  
    length = len(numbers) 
    return numbers

list1 = list

list = [12, 65, 11, 65, 2]

print(list1)
