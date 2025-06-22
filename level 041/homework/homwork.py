#შექმენით ფუნქცია, vending-machine, გექნებათ პროდუქტების სია, მომხმარებელმა, კი უნდა აირჩიოს სასურველი პროდუქტი, თქვენ კი ის უნდა დაუპრინტოთ,

#Bonus:
#თუმცა მომხმარებელს საწყისად უნდა გააჩნდეს რაღაც კონკრეტული თანხა, ხოლო პროდუქტიც რაღაც გაარკეული თანხა უნდა ღირდეს,
# თუ მომხმარებელს არ ექნება საკმარისი ფული, არ უნდა დაუპრინტოთ შესაბამისი ინდექსის პროდუქტი.

def vending_machine():
    list = ["apple", "watermelon", "peach", "strawberry", "cherry", "blueberry", "orange", "melon",]
    for i in range(len(list)):
        print(list[i])
    
    choice = int(input("choose product: "))
    if 1 <= choice <= len(list):
        print("your choice:", list[choice - 1])


vending_machine()
