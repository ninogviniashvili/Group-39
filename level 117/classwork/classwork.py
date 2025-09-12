# 1) შევქმანთ ფაილი lomi.txt და პითნის ფაილი  app.py რომელითაც მივწვდებით ./lomi.txt wrtie ფუნქციის გამოყენებთ
f = open("file.txt","r")
content = f.read()
print(f.read())


f = open("file.txt","r")
cont = f.readlines()
for i in cont:
    print(i)