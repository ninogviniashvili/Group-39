# 1. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი indexing-ის მეშვეობით გამოიტანეთ მეორე ელემენტი.
my_list = ["apple", "banana", "cherry", "date"]
print(my_list[1])  

# 2. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი შეცვალეთ მეორე ინდექსი სხვა მნიშვნელობით.
my_list = ["apple", "banana", "cherry", "date"]
my_list[1] = "blueberry"
print(my_list)

# 3. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (positive indexing).
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(my_list[0:2]) 

# 4. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (negative indexing).
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(my_list[-5:-3])

# 5. შექმენით სია, სადაც გექნებათ 6 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეოთხე ელემენტი (negative indexing & positive indexing).
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
print(my_list[0], my_list[-3])