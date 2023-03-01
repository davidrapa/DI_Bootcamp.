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

# create a human and a building
b1 = Building("123 Main St.")
h1 = Human("Alice", 25)

# move the human into the building
h1.move(b1)

# create a city and construct a new building
c1 = City("New York")
c1.construct("456 Broadway")

# get all the inhabitants of the city
all_inhabitants = c1.get_all_inhabitants()

# create some more humans and move them into the buildings
h2 = Human("Bob", 30)
h2.move(b1)
h3 = Human("Charlie", 35)
h3.move(c1.buildings[0])

# display the city info
c1.info()

