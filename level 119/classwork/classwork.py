def s(num):
    return num ** 2

result= s(5)
print(result)   

lamb = lambda num: num ** 2

result2 = lamb(5)
print(result2)

def greet(name):
    return f"hello, {name}"

greet_lamb = greet("nino")
print(greet_lamb)

greet_lamb2 = lambda name: f"hello, {name}"
result3 = greet_lamb2("nino")
print(result3)

# lambda ფუნქცია რომელსაც არ აქვს არგუმენტები მოკლე ფუნქცია, არ არის საჭირო სახელის მიცემა და გამოიყენება ერთჯერადად


numbers = list(range(1, 9))


def doub(x):
    return x * 2


doubles = list(map(doub, numbers))


def odd(x):
    return x % 2 != 0


odd = list(filter(odd, numbers))


print("og nums:", numbers)
print("doubles:", doubles)
print("odd nums:", odd)


def manual(func, lst):
    result = []
    for x in lst:
        result.append(func(x))
    return result


def manual_filter(func, lst):
    result = []
    for x in lst:
        if func(x):
            result.append(x)
    return result


manual_doubles = manual(doub, numbers)
manual_odd = manual_filter(odd, numbers)

print(manual_doubles)
print(manual_odd)
