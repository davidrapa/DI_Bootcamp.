class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1): # you can make this function in just a single line: self.animals[animal_type] = self.animals.get(animal_type, 0) + quantity
        if animal_type not in self.animals:
            self.animals[animal_type] = quantity
        else:
            self.animals[animal_type] += quantity

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal_type, quantity in self.animals.items():
            info += f"{animal_type} : {quantity}\n"
        info += "\nE-I-E-I-0!" # you can use \t to add spaces at the beginning
        return info

    def get_animal_types(self):
        animal_types = list(self.animals.keys())
        animal_types.sort()
        return animal_types

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_types_str = ", ".join(animal_types)
        return f"{self.name}'s farm has {animal_types_str}."


# testing
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
