# 1) Human კლასი
class Human:
    def speak(self):
        return "im human"

# 2) Cat კლასი
class Cat:
    def meow(self):
        return "im cat"

class Animal(Human, Cat):
    def info(self):
        return "im both"

class Batman:
    def fly(self):
        return "Batman flies"

    def fight(self):
        return "Batman fights"

class SparisMolari(Animal, Batman):
    def super(self):
        print(self.speak())  
        print(self.meow()) 
        print(self.info()) 
        print(self.fly()) 
        print(self.fight())

obj = SparisMolari()
obj.super()
