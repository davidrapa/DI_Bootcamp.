# # 🌟 Exercise 1: Cats
# # Instructions
# Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
# Instantiate three Cat objects using the code provided above.
cat1 = Cat("Tom", 3)
cat2 = Cat("Whiskers", 5)
cat3 = Cat("Garfield", 7)
# Outside of the class, create a function that finds the oldest cat and returns the cat.
def find_oldest_cat(*cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
# # # Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
# # print("The oldest cat is " + oldest_cat.name + ", and is " + str(oldest_cat.age) + " years old.")
#
# # 🌟 Exercise 2 : Dogs
# # Instructions
# #
# #
# # # Create a class called Dog.
# # class Dog:
# #     # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# #     def __init__(self, name, height):
# #         self.name = name
# #         self.height = height
# #
# #     # Create a method called bark that prints the following string “<dog_name> goes woof!”.
# #     def bark(self):
# #         print(f"{self.name} goes woof!")
# #
# #     # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# #     def jump(self):
# #         x = self.height * 2
# #         print(f"{self.name} jumps {x} cm high!")
# #
# # # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# # davids_dog = Dog("Rex", 50)
# # # Print the details of his dog (ie. name and height) and call the methods bark and jump.
# # print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
# # davids_dog.bark()
# # davids_dog.jump()
# # # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# # # Print the details of her dog (ie. name and height) and call the methods bark and jump.
# # sarahs_dog = Dog("Teacup", 20)
# # print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
# # sarahs_dog.bark()
# # sarahs_dog.jump()
# #
# #
# # # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
# # if davids_dog.height > sarahs_dog.height:
# #     print(f"{davids_dog.name} is the bigger dog.")
# # else:
# #     print(f"{sarahs_dog.name} is the bigger dog.")
#
# # 🌟 Exercise 3 : Who’s The Song Producer?
# # Instructions
# # Create an object, for example:
# # stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])#
# # Then, call the sing_me_a_song method. The output should be:
# #
# # There’s a lady who's sure
# # all that glitters is gold
# # and she’s buying a stairway to heaven
#
# # Define a class called Song, it will show the lyrics of a song.
# class Song:
#     # Its __init__() method should have two arguments: self and lyrics (a list).
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     # Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
