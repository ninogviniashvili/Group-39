
person = {
    "name": "nino",
    "hobby": "reading",
    "academy": "goa",
    "age": 100,
    "city": "tbilisi"
}

print(person.copy())

print(person.get("name"))

print(person.items())

print(person.keys())

print(person.values())

removed = person.pop("age")
print(removed)

removeditem = person.popitem()
print(removeditem)

new_info = {"hobby": "coding", "country": "georgia"}
person.update(new_info)
person.clear()
print(person)



# 2) ყველა დავალება შეასრულეთ ჯერ სტანდარტული ფორმით, შემდეგ კი შემოკლებული გზით. 1. შექმენით სია რომელშიც იქნება 0-იდან 21-მდე რიცხვები. 2. აიღეთ სია რომელშიც იქნება რიცხვების კვადრატები (თავის თავზე ნამრავლი) 1-იდან 10-მდე 3. შექმენით რიცხვების სია რომელშიც დაამატებთ ლუწ რიცხვებს 20-იდან 40-მმდე 4. შექმენით 1 რიცხვების სია, შემდეგ მორე რომელშიც გადაიტანთ მხოლოდ კენტ რიცხვებს პირბელი სიიან და გაამრავლებთ ორზე

# numbers = []
# for i in range(0, 22):
#     numbers.append(i)
# print(numbers)

numbers = [i for i in range(22)]
print(numbers)

# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

# even = []
# for i in range(20, 41):
#     if i % 2 == 0:
#         even.append(i)
# print(even)

even = [i for i in range(20, 41) if i % 2 == 0]
print(even)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd = []
# for i in numbers:
#     if i % 2 != 0:
#         odd.append(i * 2)
# print(odd)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = [i * 2 for i in nums if i % 2 == 1]
print(odd)

