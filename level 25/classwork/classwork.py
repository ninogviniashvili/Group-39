#1)
#შექმენით სია, სადაც დაამატებთ 5 ელემენტს, შემდეგ კი გამოიტანე მესამე და მეოთხე ელემენტები
subjects = ["math", "english", "science", "Physics", "Geometry"]

print(subjects[2:4])

#2)
#შექმენით სია, სადაც დაამატებთ 5 ელემენტს, შემდეგ მომხმარებელს შემოატანინეთ 
#რიცხვი და რომელ რიცხსაც შემოიტანთ მისი ინდექსი დაპრინტეთ

subjects = ["math", "english", "science", "Physics", "Geometry"]
print("Math(1), English(2), Science(3), Physics(4), Geometry(5)")
enter = int(input("enter a number for subject: "))
print(type(enter - 1))