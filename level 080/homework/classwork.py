# ```შექმენით პროექტი, სადაც ეცდებით გამოიცნოთ თქვენივე არჩეული საიდუმლო რიცხვი:

# შექმენით ფუნქციები: დაალაგოთ თქვენი კოდი ფუნქციების გამოყენებით.
# გამოიყენოთ ციკლები და პირობები: გამოიყენეთ while ციკლი, რომ გააგრძელოთ თამაში სანამ სწორ რიცხვს გამოიცნობთ. გამოიყენეთ if პირობა, რომ შეამოწმოთ, სწორია თუ არა გამოცნობილი რიცხვი.
# ყოველი გამოცნობის შემდეგ თქვენ უნდა უთხრათ მომხარებელს, მათი გმოცნობილი საიდუმლო რიცხვზე უფრო მაღალია თუ დაბალი.```


def get_secret_number():
    return 42  

def get_user_guess():
    return int(input("guess the number between 1 and 100: "))

def check_guess(secret_number, guess):
    if guess < secret_number:
        print("too low! try again.")
        return False
    if guess > secret_number:
        print("too high! try again.")
        return False
    print("congratulations! you guessed the secret number.")
    return True

def main():
    secret_number = get_secret_number()
    guessed_correctly = False
    
    while not guessed_correctly:
        user_guess = get_user_guess()
        guessed_correctly = check_guess(secret_number, user_guess)

main()

