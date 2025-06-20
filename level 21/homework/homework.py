#1. სიაში შეინახეთ 5 რიცხვი, შემდეგ კი დარპინტეთ პირველი და მეოთხე ელემენტების ნამრავლი.

num = [1 , 2, 3, 4, 5.]
print(num[0] * num[3])
#2. სიაში შეინახეთ 7 სტრინგი, შემდეგ დაპრინტეთ შუა სტრინგი.

words = ["House", "School", "Car", "Dog", "Cat", "Horse" , "Tree"]
print(words[3])
#3. ცვლადში შეინახეთ სტრინგი, შემდეგ კი დაპრინტეთ ამ სტრინგის მხოლოდ მეორე ასო.
name = "Nino"
print(name[1])
#4. შექმენით ვენდინგ მანქანის თამაში პითონის მეშვეობით, როგორც გაკვეთილზე გავაკეთე, 
#უნდა გქონდეთ პროდუქტები, მომხმარებელს უნდა შეეძლოს არჩევა რიცხვის მიხედვით, 
#შემდეგ კი უნდა დაუპრინტოს ის პროდუქტი, რომელიც ამოირჩია, პროდუქტები შეინახეთ სიაში.

print("""Products: 
      
Milk(1), Cheese(2), Cream(3), 
Apple(4), Pineaple(5), Strawberry(6), 
Potato(7), Tomato(8), Onion(9)

""")

wanted_product = int(input("Enter number: "))


shopping_list = ["Milk", "Cheese", "Cream", 
                 "Apple", "Pineapple", "Strawberry", 
                 "Potato", "Tomato", "Onion"]

print(shopping_list[wanted_product - 1])