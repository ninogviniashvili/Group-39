#1
data = [(2, "c", "hello"), (1, "a", "world"), (3, "b", "hi")]

sorted_data = sorted(data, key=lambda i: i[0])
print(sorted_data)

# 2

def welcome(name, *guest, **persn):
    print(f"welcome {name}")
    for g in guest:
        print(f"hello {g}")

print(welcome)

welcome("nino", "mari", "znd", age=25, city="tbilisi")


# arg* - ფუნქციას გადაეცემა არამიწოდებული რაოდენობის არგუმენტები, რომლებიც ფუნქციის შიგნით გადაიქცევა ტუპლად
# kvargs** - ფუნქციას გადაეცემა არამიწოდებული რაოდენობის არგუმენტები, რომლებიც ფუნქციის შიგნით გადაიქცევა ლექსიკონად

# 3

def greeting():
    print('hello nino')
greeting()