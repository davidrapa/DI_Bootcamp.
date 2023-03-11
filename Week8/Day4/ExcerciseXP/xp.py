# # 🌟 Exercise 1 : Pets
# # Instructions
#
# # Take all the cats for a walk, use the walk method.
#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Siamese(Cat):
#     pass
#
#
# bengal = Bengal('Bengie', 3)
# chartreux = Chartreux('Charlie', 4)
# # Create another cat breed named Siamese which inherits from the Cat class.
# siamese = Siamese('Sami', 2)
# # Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# all_cats = [bengal, chartreux, siamese]
# # Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# sara_pets = Pets(all_cats)
# sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
#
# Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else: # this else is redundant because you do return at the if statment
            return f"{other_dog.name} won the fight"


rex = Dog("Max", 5, 20)
pipi = Dog("Buddy", 3, 15)
max = Dog("Rocky", 7, 25)

print(rex.bark())
print(pipi.run_speed())
print(max.fight(rex))
