# 1
for i in range(1, 11):
    f = open(f"file_{i}.txt", "w")   
    f.write(f"This is file number {i}\n")
    f.close()

for i in range(1, 11):
    f = open(f"file_{i}.txt", "r")
    content = f.read()
    print(content)
    f.close()

#2

f = open("file.txt", "w")

f.write("Hello.\n")
f.write("hi\n")

f.close()

f = open("file.txt", "r")
content = f.read()
print(content)
f.close()

#3 შექმენით ფაილები და ასევე წაშალეთ იგი (მოიძიეთ ინფორამაცია)

import os
for i in range(1, 6):
    filename = f"temp_file_{i}.txt"
    with open(filename
, "w") as f:
        f.write(f"This is temporary file {i}\n")
    os.remove(filename)
    print(f"{filename} created and deleted.")
    if not os.path.exists(filename):
        print(f"{filename} successfully deleted.")
    else:
        print(f"Failed to delete {filename}.")
#4 ლუიზა დარბაიძემ იყიდა 2 ბაკალი  ლუდი ნუგზარი ჩუბინიძსითვის და ამის თაობაზე ბატნმა ნუგაზრმა განაცხადა რომ არ მეყოფა ამდენი ლუდიო 
# უნდა დავუძხო მეზობელსაც და ეღთად დავლითო 

f = open("ludi.txt", "w")
f.write("2 ბაკალი ლუდი\n")
f.close()
f = open("ludi.txt", "r")
content = f.read()
print(content)

f.close()

#5 input ის გამოოტენებით შეეკითხეთ მომხამრებელს რამდენი ლუდი ბოთლი მოითხოვა ნუზარმა რამდენსაც მოითხოვდა იმდენი ლუდის file  შექმენით და დააწერეთ თით ფაილს ludi 1 , ludi 2 და ასე შემდეგ
num_bottles = int(input("how much beer? "))
for i in range(1, num_bottles + 1):
    with open(f"ludi_{i}.txt", "w") as f:
        f.write("1 beer\n")
    print(f"ludi_{i}.txt created with 1 bottle of beer.")

#6 ულვაშებიანმა ზღვის ლომმა დაითვალა თავისი ულვაშების ღერები რაოდენობა ოღნდ როცა დაითვლიდა ამ ულვაშების რაოდენობას ავაიყდებოდა ხოლმე შედაბამისად თავიდან იწყებდა ხოლმე ულვაშების ღერების დათვლას wile loop ის გამოყენებით შექმენით იმდენი ფალი რამდნსაც ითვლიდა ეს ჩვენი ზღვის ლომი ასევე input გამოყენეთ რომ გივთხარს ყოველ ჯერზე რამდენი დათვალა ასევე 20 თუ გდაცდებოდა ულვაშების ღერების რაოდენობა მშინ  while loop გაჩერდებდ და დაწერს ტერმინშლი როპმ მაგდენი ულვაში ღერი არ აქვს ზღვის ლომს

count = 1  

while True:
    num = int(input("how much whiskers? "))

    if num > 20:
        print("not tha much whiskers")
        break


    for i in range(1, num + 1):
        f = open(f"whisker_{count}_{i}.txt", "w")
        f.write(f"this is {i} lion whiskers{count}.\n")
        f.close()

    print(f"made {num} file (დათcountვლა #{count})")
    count += 1

