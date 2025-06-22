# List Functions:

#1. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვების ჯამი.

numbers = [5, 15, 10, 30, 25]

total = sum(numbers)

print(total)

#2. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უდიდესი.

numbers = [5, 15, 10, 30, 25]

biggest = max(numbers)

print(biggest)

#3. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უმცირესი.

numbers = [5, 15, 10, 30, 25]

smallest = min(numbers)

print(smallest)

#4. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიის სიგრძე.

numbers = [5, 15, 10, 30, 25]

length = len(numbers)

print(length)

#5. შექმენით სია, 5 სტრინგით, შემდეგ .append()-ის მეშვეობით სიის ბოლოში დაამატეთ სასურველი სიტყვა.

list = ["apple", "banana", "berry", "blueberry", "orange"]

list.append("strawberry")

print(list)

#6. შექმენით სია, 5 სტრინგით, შემდეგ .insert()-ის მეშვეობით სიაში სასურველ ინდექსზე დაამატეთ სასურველი სიტყვა.

list = ["apple", "banana", "berry", "blueberry", "orange"]

list.insert(2, "lemon")

print(list)

#7. შექმენით სია, 5 სტრინგით, შემდეგ .pop()-ის მეშვეობით სიიან ამოაგდეთ ინდექსის მეშვეობით რომელიმე სიტყვა.

list = ["apple", "banana", "berry", "blueberry", "orange"]

list.pop(3)

print(list)