import random


class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10

    def basic_attack(self, other):
        other.life -= self.attack
        print(f"{self.name} attacks {other.name} for {self.attack} damage!")


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        self.life += 10
        self.attack -= 2
        print(f"{self.name} the Druid appears!")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} meditates and gains 10 life but loses 2 attack!")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} summons an animal to aid in battle, gaining 5 attack!")

    def fight(self, other):
        damage = int(0.75 * self.life + 0.75 * self.attack)
        other.life -= damage
        print(f"{self.name} fights {other.name} for {damage} damage!")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} the Warrior appears!")

    def brawl(self, other):
        damage = 2 * self.attack
        other.life -= damage
        self.life += int(0.5 * self.attack)
        print(f"{self.name} brawls with {other.name} for {damage} damage and gains {int(0.5 * self.attack)} life!")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} trains hard and gains 2 attack and 2 life!")

    def roar(self, other):
        other.attack -= 3
        print(f"{self.name} roars, intimidating {other.name} and lowering their attack by 3!")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} the Mage appears!")

    def curse(self, other):
        other.attack -= 2
        print(f"{self.name} curses {other.name}, lowering their attack by 2!")

    def summon(self):
        self.attack += 3
        print(f"{self.name} summons magical power, gaining 3 attack!")

    def cast_spell(self, other):
        damage = int(self.attack / 5)
        other.life -= damage
        print(f"{self.name} casts a spell on {other.name} for {damage} damage!")


# Testing the classes
druid = Druid("Nimue")
warrior = Warrior("Conan")
mage = Mage("Gandalf")

# Basic attacks
druid.basic_attack(warrior)
warrior.basic_attack(mage)
mage.basic_attack(druid)

# Druid actions
druid.meditate()
druid.animal_help()
druid.fight(warrior)

# Warrior actions
warrior.brawl(mage)
warrior.train()
warrior.roar(mage)

# Mage actions
mage.curse(warrior)
mage.summon()
mage.cast_spell(druid)

