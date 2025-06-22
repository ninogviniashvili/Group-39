
#1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.
def num(number):
    return number + 5
result = num(10)
print(result)


#2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

def multiply(a, b):
    return a * b
result = multiply(4, 5)
print(result)

#3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).

def model(VS):
    return len(VS)
result = model("Adriana Lima")
print(result) 

#4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

def word(strings):
    return len(strings)

result = word(["hello", "world", "python"])
print(result)  


#5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome 
# (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.

def word(s):
    return s == s[::-1] 


print(word("racecar"))  
print(word("hello"))


#6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
#(მაგალითად: input: "Hello World". output: "HELLO WORLD".

def word(s):
    return s.upper()
print(word("Hello"))