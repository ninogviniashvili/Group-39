class Character:
    _count = 0

    def __init__(self, name, health, damage, speed, level=1):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.level = level
        Character._count += 1

    @staticmethod
    def count_characters():
        return Character._count

    def __str__(self):
        return f"{self.name} (Level {self.level}) - HP:{self.health}, DMG:{self.damage}, SPD:{self.speed}"

ninja = Character("Ninja", 80, 15, 30)
samurai = Character("Samurai", 100, 20, 20)
viking = Character("Viking", 120, 25, 15)
warrior = Character("Warrior", 110, 22, 18)
veteran = Character("Veteran", 90, 18, 22)
tribesman = Character("Tribesman", 85, 17, 25)
necromancer = Character("Necromancer", 70, 30, 10)

assassin = Character("Assassin", 75, 28, 35)
paladin = Character("Paladin", 130, 20, 12)

print("Total characters created:", Character.count_characters())

for c in [ninja, samurai, viking, warrior, veteran, tribesman, necromancer, assassin, paladin]:
    print(c)
