#1. შექმენით ფუნქცია, სადაც გექნებათ 5 სიტყვიანი სია, შემდეგ მომხმარებელს შემოატანინეთ 0-იდან 5-მდე რიცხვი, 
# და დაუპრინტეთ ეგ index თქვენი შექმნილი სიიდან.3
number = ["num1", "num2", "num3", "num4", "num5"]
def list(idk):

    if 0 < idk < 5:
        print(number[idk])
    else:
        print("incorrect number")

num123 = int(input("enter number from 0 to 5: "))
list(num123)




 