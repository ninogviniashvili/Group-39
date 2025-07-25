# 2) შექმენით set სახელად numbers, დაამატეთ მას ორი რიცხვი add() მეთოდით და წაშალეთ ორი ელემენტი remove() მეთოდით. შემდეგ შექმენით მეორე set სახელად even_numbers და გამოიყენეთ union(), intersection(), difference() ორივე set-ზე. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი

numbers = set()
numbers.add(5)
numbers.add(10)
print(numbers)
numbers.remove(5)
numbers.remove(10)
print(numbers)
even_numbers = {2, 4, 6, 8, 10}
union_set = numbers.union(even_numbers)
print("Union:", union_set)
intersection_set = numbers.intersection(even_numbers)
print("Intersection:", intersection_set)
difference_set = numbers.difference(even_numbers)
print("Difference:", difference_set)

# 3) დაწერეთ ფუნქცია, რომელიც იღებს set-ს, ამატებს მას 3 ელემენტს add() მეთოდით, შემდეგ შლის ერთ ელემენტს remove() მეთოდით და აბრუნებს საბოლოო შედეგს



def modify_set(input_set):
    input_set.add(1)
    input_set.add(2)
    input_set.add(3)
    print("Set after adding elements:", input_set)
    input_set.remove(1)
    print("Set after removing an element:", input_set)
    return input_set

print(modify_set({4, 5, 6}))

# 4) შექმენით dictionary სახელად student, დაამატეთ მას მონაცემები: name, hobby, height, weight. შემდეგ გამოიყენეთ .get() მეთოდი name-ის მისაღებად და .pop() მეთოდი height-ის წასაშლელად. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი
student = {
    "name": "leonardo",
    "hobby": "reading",
    "height": 180,
    "weight": "1308"
}
print(student.get("name"))
print(student)
print(student.pop("height"))
print(student)


# 5) დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და აბრუნებს მის keys-სა და values-ს .keys() და .values() მეთოდებით. დაბეჭდეთ ორივე შედეგი და დაურთეთ კომენტარები
def get_dict_keys_values(input_dict):
    keys = input_dict.keys()
    values = input_dict.values()
    print("Keys:", keys)
    print("Values:", values)
    return keys, values

print(get_dict_keys_values(student))


# 6) შექმენით ლექსიკონი person და გამოიყენეთ .items() მეთოდი, რათა დაბეჭდოთ ყველა key და value წყვილად. გამოიყენეთ loop და კომენტარი დაუმატეთ შედეგს

person = {
    "name": "aleqsandre",
    "age": 30,
    "city": "china"
}
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
print(person.items()) 

# 7) შექმენით ლექსიკონი animal, შექმენით მისი ასლი .copy() მეთოდით, შემდეგ კი გამოიყენეთ .clear() ორივეზე (დასაწყისში და ბოლოს დაბეჭდეთ ორივე ლექსიკონი, კომენტარით)

animal = {
    "type": "dog",
    "breed": "labrador",
    "age": 5
}
animal_copy = animal.copy()
print("Original animal dictionary:", animal)
print("Copied animal dictionary:", animal_copy)
animal.clear()
print(animal)
print(animal_copy)
print(animal)
print(animal_copy)

# 8) დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და ამატებს ახალ წყვილს ('age': 14) .update() მეთოდით, შემდეგ კი შლის ბოლო ელემენტს .popitem() მეთოდით. დაბეჭდეთ შედეგი და დაუმატეთ კომენტარები

def update_and_popitem(input_dict):
    input_dict.update({'age': 14})
    print(input_dict)
    removed_item = input_dict.popitem()
    print(removed_item)
    return input_dict
print(update_and_popitem({"name": "iuli", "hobby": "gaming"}))

# 9) რიცხვების სიიდან "numbers = [1, 4, 7, 10, 13, 16, 19]" აირჩიეთ მხოლოდ კენტები, გაამრავლეთ ორზე და დაამატეთ "new_list"-ში, ჯერ "for"-ით, შემდეგ list comprehension-ით. ბოლოს გააკეთეთ 2 მსგავსი მაგალითი: ერთში მხოლოდ მოქმედება გამოიყენეთ, მეორეში მხოლოდ პირობა
numbers = [1, 4, 7, 10, 13, 16, 19]
odd = []
for i in numbers:
    if i % 2 != 0:
        odd.append(i * 2)
print(odd)

odd = [i * 2 for i in numbers if i % 2 != 0]
print(odd)
new_list = [i * 2 for i in numbers if i % 2 != 0]
print(new_list)

# 10) სიტყვების სიიდან "words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']" შეარჩიეთ მხოლოდ ისინი, რომლების სიგრძე მეტია 5-ზე, ჯერ "for"-ით, შემდეგ list comprehension-ით
words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
print(long_words)

long_words = [word for word in words if len(word) > 5]
print(long_words)

# 11) რიცხვების სიიდან "nums = list(range(1, 21))" შექმენით ახალი სია კვადრატებით, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ სცადეთ მსგავსი მაგალითი სხვა მოქმედებით
nums = list(range(1, 21))
squares = []
for num in nums:
    squares.append(num ** 2)
print(squares)
squares = [num ** 2 for num in nums]
print(squares)
squares = [num ** 3 for num in nums]  # სხვა მოქმედება: კუბი
print(squares)

# 12) სიიდან "mixed = [2, 5, 8, 11, 14, 17, 20]" შექმენით ორი სია list comprehension-ით: ერთში მხოლოდ ლუწები, მეორეში — კენტები

mixed = [2, 5, 8, 11, 14, 17, 20]
evens = [num for num in mixed if num % 2 == 0]

# 13) სიიდან "animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']" შექმენით ახალი სია, რომელიც შეიცავს სიტყვების პირველ ასოებს, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ აირჩიეთ მხოლოდ ის სიტყვები, რომლებიც "e"-ზე იწყება\

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']

first_letters_for = []
for animal in animals:
    first_letters_for.append(animal[0])

first_letters_lc = [animal[0] for animal in animals]

e_animals_for = []
for animal in animals:
    if animal.startswith('e'):
        e_animals_for.append(animal)

e_animals_lc = [animal for animal in animals if animal.startswith('e')]

print(first_letters_for)
print(first_letters_lc)
print(e_animals_for)
print(e_animals_lc)


# 14) სცადეთ რიცხვი გაყვოთ ნულზე, გამოიყენეთ "try" და "except" რათა თავიდან აიცილოთ შეცდომა და დაბეჭდოთ „ნულზე გაყოფა არ შეიძლება“

try:
    number = 10
    result = number / 0
except:
    print("no devision")


# 15) სიიდან "my_list = [5, 10, 15]" სცადეთ დაბეჭდოთ ელემენტი არარსებულ ინდექსზე. გამოიყენეთ "try" და "except" რომ პროგრამა არ გაჩერდეს და გამოჩნდეს შეტყობინება „ინდექსი არასწორია“
my_list = [5, 10, 15]

try:
    print(my_list[5])
except:
    print("wrong index")

# 16) სთხოვეთ მომხმარებელს შეიყვანოს რიცხვი "input()"-ით და გადააკეთეთ "int"-ად. გამოიყენეთ "try" და "except", რომ გაუმკლავდეთ შეცდომას თუკი სიმბოლოები შეიყვანეს. დაბეჭდეთ „შეიყვანეთ მხოლოდ რიცხვი“

try:
    user_input = input("enter number: ")
    number = int(user_input)
    print(number)
except:
    print("only one number")
