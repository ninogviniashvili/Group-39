# 1
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        """add to balance, only if amount is positive"""
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        """remove from balance if enough funds"""
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            print("Not enough funds")
            return False

    def get_balance(self):
        """returns current balance"""
        return self._balance


account = BankAccount(100)

account.deposit(50)

account.withdraw(30)

print(account.get_balance())

# _balance არის "private" ატრიბუტი, ანუ გარედან პირდაპირ არ უნდა შეცვალო.
# ამის ნაცვლად გამოიყენება მეთოდები (deposit, withdraw, get_balance) უსაფრთხო წვდომისთვის.

# 2
class MathUtil:
    # Static method: მეთოდი, რომელიც არ არის მიბმული ობიექტთან და არ საჭიროებს self
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(MathUtil.add(5, 3))
print(MathUtil.multiply(4, 6))

# @staticmethod საშუალებას აძლევს ფუნქციას კლასის ნაწილად დარჩეს,
# მაგრამ არ აქვს წვდომა კლასის ან ობიექტის მონაცემებზე.
# ანუ შესაძლებელია ვიქენოთ MathUtil.add(...) ან MathUtil.multiply(...) ობიექტის შექმნის გარეშე.

# 3
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.sound()
cat.sound()

# პოლიმორფიზმი ნიშნავს, რომ ერთსა და იმავე სახელის მეთოდი
# (sound) სხვადასხვა კლასებში განსხვავებულ ქცევას ავლენს.
# აქ Animal-ის sound მეთოდი არის საერთო, ხოლო Dog და Cat
# მას "override"-ს უკეთებენ საკუთარ საჭიროებებზე.

# 5

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

@staticmethod
def discount(price, percent):
    """returns price after applying discount"""
    return price * (1 - percent / 100)

class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def show_products(self):
        for product in self._products:
            print(f"{product.name}: ${product.price:.2f}")


p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 50)

p1.price = Product.discount(p1.price, 10)  # 10% off
p2.price = Product.discount(p2.price, 20)  # 20% off

order = Order()
order.add_product(p1)
order.add_product(p2)
order.show_products()


# Data hiding: _products არის "private" attribute, გარედან პირდაპირი წვდომა არ გექნება.
# Staticmethod: discount შეიძლება გამოვიძახოთ კლასიდან პირდაპირ Product.discount(...),
# ობიექტის შექმნის გარეშე, რადგან არ საჭიროებს self-ს.
