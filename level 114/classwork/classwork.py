items = ["Math", "Physics", "Chemistry", "Biology"]

# ამატებს ახალ ელემენტს სიის ბოლოს
items.append("History")
print( items)

# ამატებს ელემენტს მითითებულ პოზიციაზე
items.insert(2, "Geography") 
print(items)

# შლის და აბრუნებს ბოლო ელემენტს
removed = items.pop()
print(items)
print(removed)

numbers = [42, 3, 19, 8, 27]

# ალაგებს სიას ზრდადობით
numbers.sort()
print(numbers)

# აბრუნებს მინიმალურ მნიშვნელობას სიიდან
print(min(numbers))

# აბრუნებს მაქსიმალურ მნიშვნელობას სიიდან
print(max(numbers))





vegetables = ("carrot", "tomato", "cucumber", "potato", "onion", "pepper")

print(len(vegetables))

sorted = sorted(vegetables)
print(sorted)

v1, v2, v3, *rest = vegetables

print(v1)
print(v2)
print(v3)
print(rest)





set1 = {1, 2, 3, 4, 5, 5, 3}
set2 = {4, 5, 6, 7, 8, 4, 6} 


print(set1)
print(set2)


set1.add(10)
set2.add(20)

print(set1)
print(set2)


set1.remove(2)  
set2.remove(7)  

print(set1)
print(set2)


union_set = set1.union(set2)
print( union_set)


intersection_set = set1.intersection(set2)
print(intersection_set)


difference_set = set1.difference(set2)
print(difference_set)
