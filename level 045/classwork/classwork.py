#1. შექმენით სია, სადაც გექნებათ სიტყვები, შემდეგ გამოიტანეთ სათითაოდ ყველა სიტყვა.

words = ["lemon", "banana", "strawberry", "kiwi", "melon"]

for word in words:
    print(word)

#2. შექმენით სია, სადაც გექნებათ 5 ცალი რიცხვი, შემდეგ გამოიტანეთ სათითაოდ ყველა რიცხვი.

numbers = [5, 10, 15, 20, 25]

for number in numbers:
    print(number)

#3. შექმენით სია, სადაც გექნებათ` 5 ცალი რიცხვი, შემდეგ გამოიტანეთ სათითაოდ ყველა რიცხვი გამრავლებული თავის თავზე.

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    num = number * number
    print(num)


#4. შექმენით სია, სადაც გექნებათ 5 ცალი რიცხვი, შემდეგ ეს ციფრები გააორმაგეთ და დაამატეთ ახალ სიაში.

numbers = [1, 2, 3, 4, 5]

num = []
for number in numbers:
    num.append(number * 2)


print(num)
