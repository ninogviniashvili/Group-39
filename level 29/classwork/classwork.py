#შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა

subjects = ["math", "english", "art", "PE"]
print(len(subjects))
movies = ["Avatar", "Harry Potter", "spider man", "Avengers"]

actors = ["Maggie Smith, Emma Watson", "Johnny Depp", "Brad Pitt"]
names = ["nino", "mari", "elene", "nini", "nino1",]


#შექმენთ 2 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 3-3 ცვლადი

movies = ["Avatar", "Harry Potter", "spider man", "Avengers"]
movies.append("barbie")
print(movies)
actors = ["Maggie Smith, Emma Watson", "Johnny Depp", "Brad Pitt"]
actors.append("Angelina Jolie")
print(actors)
names = ["nino", "mari", "elene", "nini", "nino",]
names.append("lizi")
print(names)


#შექმენით 2 ლისტი. პირველს მე5ე და მე2ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე3ე და მე4ე ადგილას

movies = ["Avatar", "Harry Potter", "spider man", "Avengers", "The devil wears prada"]
movies.insert(1, "Gilmore girls")
movies.insert(4, "Maleficent")
print(movies)

actors = ["Maggie Smith, Emma Watson", "Johnny Depp", "Brad Pitt"]
actors.insert(2, "Nicole Kidman")
actors.insert(3, "Anne Hathaway")
print(actors)


#```შექმენით 2 ლისტი და ორივედან ამოშალეთ 2-2 ცვლადი pop ფუნქციის გამოყენებით```

subjects = ["math", "english", "art", "PE"]
subjects.pop(1)
subjects.pop(3)
print(subjects)

names = ["nino", "mari", "elene", "nini", "nino1",]
names.pop(2)
names.pop(4)
print(names)

#```შექმენით 1 ლისტი და გამოიყენეთ ყველა ფუნქცია რაც დღეს გავიარეთ```
actors = ["Maggie Smith, Emma Watson", "Johnny Depp", "Brad Pitt"]
actors.append
print(actors)















#შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში
name = "nino"
print(len(name))
name1 = "nini"
print(len(name1))
name2 = "elene"
print(len(name2))