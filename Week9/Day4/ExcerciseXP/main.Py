# 🌟 Exercise 1 : Human
# Instructions
# Create a class Human, it has the following attributes:
# name (str)
# age (int)
# living_place (Building - Default is None)
#
# Create another class Building, it has the following attributes:
# address (str)
# inhabitants (List of Human objects - Default is empty)
#
# Create a class City, it has the following attributes:
# name (str)
# buildings (List of Building objects - Default is empty)
#
# Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.
# Created objects and call the methods

class Human:
    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)


class Building:
    def __init__(self, address, inhabitants=[]):
        self.address = address
        self.inhabitants = inhabitants


class City:
    def __init__(self, name, buildings=[]):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        new_building = Building(address)
        self.buildings.append(new_building)

    def info(self):
        num_buildings = len(self.buildings)
        total_age = 0
        for building in self.buildings:
            for inhabitant in building.inhabitants:
                total_age += inhabitant.age
        mean_age = total_age / len(self.get_all_inhabitants())
        print(f"The city of {self.name} has {num_buildings} buildings and a mean age of {mean_age:.1f} years.")

    def get_all_inhabitants(self):
        all_inhabitants = []
        for building in self.buildings:
            all_inhabitants.extend(building.inhabitants)
        return all_inhabitants


b1 = Building("123 Main St.")
h1 = Human("Alice", 25)


h1.move(b1)

# construct a new building
c1 = City("New York")
c1.construct("456 Broadway")


all_inhabitants = c1.get_all_inhabitants()

 # humans  into the buildings
h2 = Human("Bob", 30)
h2.move(b1)
h3 = Human("Charlie", 35)
h3.move(c1.buildings[0])


c1.info()
