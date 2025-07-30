# 2) სცადეთ რიცხვი გაყვოთ ნულზე. გამოიყენეთ "try" და "except" რათა თავიდან აიცილოთ შეცდომა და დაბეჭდოთ „ნულზე გაყოფა არ შეიძლება“

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero")

# 3) სიიდან "my_list = [5, 10, 15]" სცადეთ დაბეჭდოთ ელემენტი არარსებულ ინდექსზე. გამოიყენეთ "try" და "except" რომ პროგრამა არ გაჩერდეს და გამოჩნდეს შეტყობინება „ინდექსი არასწორია“

my_list = [5, 10, 15]
try:
    print(my_list[5])
except IndexError:
    print("index is out of range")

# 4) სთხოვეთ მომხმარებელს შეიყვანოს რიცხვი "input()"-ით და გადააკეთეთ "int"-ად. გამოიყენეთ "try" და "except", რომ გაუმკლავდეთ შეცდომას თუკი სიმბოლოები შეიყვანეს. დაბეჭდეთ „შეიყვანეთ მხოლოდ რიცხვი“
try:
    num = int(input("enter a number:"))
except ValueError:
    print("ONLY NUMBERS")

# 5) შექმენით ფუნქცია, რომელიც მიიღებს ორ რიცხვს და დააბრუნებს მათ გაყოფას. გამოიყენეთ "try", "except" და დაამატეთ "else" რათა წარმატებულ შემთხვევაში დაბეჭდოს „გაყოფა წარმატებით შესრულდა“, ხოლო შეცდომისას — შესაბამისი შეტყობინება

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "You can't divide by zero"
    else:
        return f"Division successful: {result}"
    finally:
        print("End of division operation")

    return result

# 6) შექმენით ფუნქცია, რომელიც მიიღებს ერთ რიცხვს. თუ რიცხვი უარყოფითია, გამოიყენეთ "raise ValueError" შესაბამისი შეტყობინებით, მაგალითად: "რიცხვი არ შეიძლება იყოს უარყოფითი"

def check_positive_number(num):
    if num < 0:
        raise ValueError("Number cannot be negative")
    return f"Number is positive: {num}"


# 7) შექმენით კოდი, სადაც გამოიყენებთ "try", "except" და "finally". მაგალითად, გახსენით ფაილი, წაიკითხეთ შიგთავსი, და გამოიყენეთ "finally", რომ ყოველთვის დაიხუროს ფაილი მიუხედავად იმისა მოხდა თუ არა შეცდომა

try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("This will always execute")

# 8) შექმენით ციკლი, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი მანამ სანამ სწორად არ შეიყვანს. გამოიყენეთ "try" და "except", რომ თავიდან აიცილოთ შეცდომა, და დაბეჭდეთ შეტყობინება არასწორი შეყვანისას

while True:
    try:
        number = int(input("please enter number: "))
    except ValueError:
        print("wrong input enter number")
    else:
        break

print(number)


# 9) შექმენით სია რიცხვებით და სცადეთ თითოეული რიცხვი გადააქციოთ float ტიპად. გამოიყენეთ "try" და "except", რათა ტექსტის შემთხვევაშიც კოდი არ გაჩერდეს და უბრალოდ გამოტოვოს შეცდომიანი ელემენტი
items = ["10", "5.5", "abc", "7", "xyz", "3.14"]
converted = []

for item in items:
    try:
        num = float(item)
    except ValueError:
        pass  # შეცდომის შემთხვევაში არაფერი ვაკეთებთ
    else:
        converted.append(num)

print(converted)

# 10) შექმენით პროგრამა, რომელიც იღებს სია "values = ['10', '20', 'hello', '30']"-ს და თითოეულს ცდის გადააქციოს int ტიპად. შეცდომის შემთხვევაში დაბეჭდეთ „მონაცემი არ არის რიცხვი: ...“ და გააგრძელეთ ციკლი

values = ['10', '20', 'hello', '30']
for value in values:
    try:
        num = int(value)
    except ValueError:
        print(f"Data is not a number: {value}")
    else:
        print(f"Converted value: {num}")
