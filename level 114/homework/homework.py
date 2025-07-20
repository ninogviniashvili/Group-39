# 2)
def manual_index(lst, element):
    for index, item in enumerate(lst):
        if item == element:
            return index
    return -1  

my_list = ['a', 'b', 'c', 'd']
print(manual_index(my_list, 'c'))
print(manual_index(my_list, 'z'))

# 3)
def manual_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
my_list = ['a', 'b', 'c', 'a', 'd', 'a']
print(manual_count(my_list, 'a'))

# 4) 
fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi']
colors = ['red', 'blue', 'green', 'blue', 'yellow']
numbers = [4, 1, 7, 3, 9, 1, 4]

# index - აბრუნებს პირველი ელემენტის ინდექსს
print(fruits.index('apple'))

# count - რამდენჯერ გვხვდება კონკრეტული ელემენტი
print(fruits.count('apple'))

# sort - აწყობს სიას ზრდადობით 
fruits.sort()
print(fruits) 

# sorted - აწყობს სიას მაგრამ ქმნის ახალ სიას (თავდაპირველი არ იცვლება)
fruits2 = ['apple', 'banana', 'orange']
print(sorted(fruits2))  
print(fruits2) 

# min - აბრუნებს ანბანის მიხედვით პირველ ელემენტს
print(min(fruits2)) 

# max - აბრუნებს ანბანის მიხედვით ბოლო ელემენტს
print(max(fruits2))  


print(colors.index('blue')) 
print(colors.count('blue'))  
colors.sort()
print(colors)               
print(sorted(colors))         
print(min(colors))           
print(max(colors))         

print(numbers.index(1))      
print(numbers.count(4))       
numbers.sort()
print(numbers)                
print(sorted(numbers))        
print(min(numbers))           
print(max(numbers))           


# 5) 
def unique_elements_count(lst):
    unique_elements = set(lst)
    for element in unique_elements:
        print(f"{element} - {lst.count(element)}")
unique_elements_count(fruits)
unique_elements_count(colors)
unique_elements_count(numbers)

# 6) 
animals = ('dog', 'cat', 'horse', 'dog', 'fish')

print(animals.index('dog'))
print(animals.count('dog'))


# 7) 
def tuple_info(tup):
    print(f"Length: {len(tup)}")
    print(f"First element: {tup[0]}")
    print(f"Last element: {tup[-1]}")
tuple_info(animals)


# 8) 
person_info = ('Nino', 17, 'Paris')
name, age, country = person_info
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")


# 9) 
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)
new_list = list(my_tuple)
print(new_list)
print(type(my_tuple))


# 10)
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.add(7)
print(numbers)
numbers.remove(2)
numbers.remove(4)
print(numbers)
even_numbers = {2, 4, 6, 8, 10}
union_set = numbers.union(even_numbers)
print(union_set)
intersection_set = numbers.intersection(even_numbers)
print(intersection_set)
difference_set = numbers.difference(even_numbers)
print(difference_set)


# 11) 
def modify_set(s):
    s.add(10)
    s.add(20)
    s.add(30)
    s.remove(1)
    return s
my_set = {1, 2, 3, 4, 5}
print(modify_set(my_set))
