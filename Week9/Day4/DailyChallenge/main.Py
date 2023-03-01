class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food):
        if food in self.likes:
            return f"{self.name} eats the {food} and loves it!"
        elif food in self.hates:
            return f"{self.name} eats the {food} and hates it!"
        else:
            return f"{self.name} eats the {food}!"


p1 = Person("Mario", ["Asado"], ["Empanadas"])


print(p1.taste("Asado"))
print(p1.taste("Empanadas"))     # Sam eats the cheese!

