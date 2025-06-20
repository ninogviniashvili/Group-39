#1. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ string-ს, შემდეგ შეაერთეთ ისინი და დაპრინტეთ.

def word(str1, str2):

    result = str1 + str2

    print(result)

word("Hello, ", "GOA!")


#2. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ 5 ელემენტიან რიცხვების სიას, შემდეგ დაპრინტეთ სიის მე-3 ელემენტისა და მე-4 ელემენტის ჯამი.

def num(numbers):

    result = numbers[2] + numbers[3]

    print(result)

num([10, 20, 30, 40, 50])


#3. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ მანძილს კილომეტრში, შემდეგ გადააქციეთ ის მეტრში და დაპრინტეთ.

def kilometers_to_meters(kilometers):

    meters = kilometers * 1000

    print(str(kilometers) + " kilometers = " + str(meters) + " meter")

kilometers_to_meters(5)


#4. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ რიცხვს, შემდეგ დაპრინეთ ამ ორი რიცხვიდან უფრო დიდი.

def larger_number(num1, num2):

    if num1 > num2:
        print(num1)
    else:
        print(num2)


larger_number(10, 20)


#5. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ სტრინგს, შემდეგ შეაბრუნეთ ეს სტრინგი და დაპრინტეთ.

def word(inverted):

    word = inverted[::-1]

    print(word)

word("Hello!")

