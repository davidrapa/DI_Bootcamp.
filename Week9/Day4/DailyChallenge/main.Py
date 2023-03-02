# Instructions :
# Create a Person class which will have three properties:
# Name
# List of foods they like
# List of foods they hate
# Note: A person can have an empty list for foods they hate and/or love.
#
# In this class, create the method taste():
# It will take in a food name as a string.
# Return {person_name} eats the {food_name}.
# If the food is in the person’s like list, add ‘and loves it!’ to the end.
# If it is in the person’s hate list, add ‘and hates it!’ to the end.
# If it is in neither list, simply add an exclamation mark to the end.

class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food):
        if food in self.likes:
            return f"{self.name} eats the {food} and loves it!"
        elif food in self.hates: # there is no need for the elif here, olease change it with if
            return f"{self.name} eats the {food} and hates it!"
        else:
            return f"{self.name} eats the {food}!"


p1 = Person("Mario", ["Asado"], ["Empanadas"])


print(p1.taste("Asado"))
print(p1.taste("Empanadas"))  

