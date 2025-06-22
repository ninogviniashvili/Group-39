# მოცემული გაქვთ სია:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# თქვენი დავალებაა ამ სიიდან დაპრინტოთ მხოლოდ გაორმაგებული ლუწი რიცხვები,

# მაგალითად: 4, 8, 12...

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
#         print(num * 2)




num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0  
odd = 0

for number in num:
    if number % 2 == 0:
        even += number

    else:  
        odd += number
done = even - odd
print(done)
