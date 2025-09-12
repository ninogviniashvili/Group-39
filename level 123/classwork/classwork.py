# 1
class Person:
    def __init__(self, name, surname, age, work):
        self.name = name
        self.surname = surname
        self.age = age
        self.work = work

    def working(self):
        print(f"{self.name} working at {self.work}")


class Student(Person):
    def __init__(self, name, surname, age, work, year):
        super().__init__(name, surname, age, work)
        self.year = year

    def working(self):
        print("studying")


p1 = Person("nino", "gviniashvili", 19, "iafa")
p2 = Student("luka", "gviniashvili", 23, "fnakf", )

print(p1.name, p1.age)
print(p2.name, p2.year)

p1.working()
p2.working()

# 2

class Person:
    def __init__(self, name, surname, age, work, birth_year, id_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.work = work
        self._birth_year = birth_year
        self.__id = id_number

    def working(self):
        print(f"{self.name} working at {self.work}")

    def get_id(self):
        return self.__id


class Student(Person):
    def __init__(self, name, surname, age, work, year, birth_year, id_number):
        super().__init__(name, surname, age, work, birth_year, id_number)
        self.year = year

    def working(self):
        print("studying")


p1 = Person("nino", "gviniashvili", 18, "no", 2007, 111123)
p2 = Student("luka", "gviniashvili", 23, "agmjg", 2002, 193212)

print(p1._birth_year)

print(p1._Person__id)

print(p2._Person__id)
