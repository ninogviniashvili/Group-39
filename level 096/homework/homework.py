# შექმენით ფუნქცია, რომელიც იღებს რიცხვების ჩამონათვალს და აბრუნებს ახალ სიას, სადაც თითოეული რიცხვი მრავლდება 2-ზე, for loop და .append()-ის გამოყენებით.

def multiply_by_two(sia):
    result = []
    for ricxvi in sia:
        result.append(ricxvi * 2)
    return result

print(multiply_by_two([1, 2, 3, 4])) 

# შექმენით პროგრამა, სადაც მომხმარებელს შეატანინებთ რიცხვს 5-ჯერ, დაამატებთ მათ სიაში და დაბეჭდავთ შებრუნებულ სიას.

nums = []
for i in range(5):
    num = int(input("number: "))
    nums.append(num)

reverse = []
for i in range(4, -1, -1):
    reverse.append(nums[i])

print(reverse)

# 3. 

def wordlength(words):
    lengths = []
    for s in words:
        lengths.append(len(s))
    return lengths

print(wordlength(["chess", "bike", "horse"])) 

# 5

def exept(lst):
    new = []
    for o in lst:
        if len(o) > 3:
            new.append(o)
    return new


print(exept(["alax", "bajan", "mamajan", "hello", "janebi"]))  
