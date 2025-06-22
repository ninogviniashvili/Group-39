# დაწერეთ ფუნქცია, რომელიც მიიღებს სტრინგს სადაც იქნება წინადადება და დააბრუნებს ინდივიდუალური სიტყვების სიას split()-ის გამოყენებით.
def split_sentence(sentence):
    return sentence.split()

print(split_sentence("Hello world! This is a test."))


# დაწერეთ ფუნქცია, რომელიც მიიღებს სიტყვების სიას და დააბრუნებს ერთ სტრიქონს, სადაც სიტყვები შეერთებული იქნება ტირეებით join()-ის გამოყენებით.

def join_words(words):
    return ' '.join(words)
print(join_words(['Hello', 'world!', 'This', 'is', 'a', 'test.']))


# გამოიყენეთ enumerate() ელემენტების სიაზე ციკლით გადასავლელად და თითოეული ელემენტის ინდექსით დასაბეჭდად.

def print_with_index(words):
    for index, word in enumerate(words):
        print(f"Index: {index}, Word: {word}")
print_with_index(['Hello', 'world!', 'This', 'is', 'a', 'test.'])


# სთხოვეთ მომხმარებელს შემოიტანოს წინადადება, შემდეგ დაყავით იგი სიტყვებად და დაბეჭდეთ თითოეული სიტყვა.

def print_words_from_input():
    sentence = input("Please enter a sentence: ")
    words = split_sentence(sentence)
    for word in words:
        print(word)
print_words_from_input()


# შექმენით პროგრამა, რომელიც იღებს პროდუქტების სახელების სიას და აკავშირებს მათ ერთ მძიმით, join()-ის გამოყენებით.

def join_names(product_names):
    return ', '.join(product_names)
print(join_names(['Apples', 'Bananas', 'Cherries', 'Dates']))