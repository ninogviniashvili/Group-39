#1. შექმენით სია, სადაც გექნებათ თქვენი მეგობრების სახელები, შემდეგ დაპრინტეთ პირველი 
# ორი მეგობრის სახელი.
print("names : Mari(1), Nini(2), Elene(3), Nino(4), Gio(5), Dati(6).")

names = ["Mari", "Nini", "Elene", "Nino", "Gio", "Dati"]

chosen_name1 = int(input("enter name number : "))
chosen_name2 = int(input("enter second name number : "))

print(names[chosen_name1 - 1])
print(names[chosen_name2 - 1])
