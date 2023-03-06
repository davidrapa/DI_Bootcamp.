# Vaccines Management System
# Your goal is to create a program to help a city with the vaccination of its citizens.
#
#
#
# Part 1
# You will have to create two classes:
# Human
# Queue
#
#
# Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.
#
# This class has no methods.
#
#
#
# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
#
# This class is useful to manage who will get vaccinated in priority. It has the following methods:
#
# add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.
#
# find_in_queue(self, person) : Returns the index of a human in the queue.
#
# swap(self, person1, person2): Swaps person1 with person2.
#
# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
#
# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.
#
# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people
# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).
#
# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.
class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.priority or person.age >= 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i].id_number == person.id_number:
                return i
        return -1

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 != -1 and index2 != -1:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if self.humans:
            if self.humans[0].priority or self.humans[0].age >= 60:
                return self.humans.pop(0)
            else:
                return self.sort_by_age_helper(self.humans.pop(0))
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                if self.humans[i].priority or self.humans[i].age >= 60:
                    return self.humans.pop(i)
                else:
                    return self.sort_by_age_helper(self.humans.pop(i))
        return None

    def sort_by_age(self):
        priority_people = []
        older_people = []
        younger_people = []

        for i in range(len(self.humans)):
            if self.humans[i].priority:
                priority_people.append(self.humans[i])
            elif self.humans[i].age >= 60:
                older_people.append(self.humans[i])
            else:
                younger_people.append(self.humans[i])

        self.humans = priority_people + older_people + younger_people

    def sort_by_age_helper(self, person):
        if person.priority or person.age >= 60:
            return person
        else:
            self.humans.append(person)
            self.sort_by_age()
            return self.humans.pop(0)





# Part 2
# Human
# Create an attribute family for the Human class.
#
# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.
#
#
#
# Queue
# Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.
class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for i, p in enumerate(self.humans):
            if p.id_number == person.id_number:
                return i
        return None

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 is not None and index2 is not None:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if self.humans:
            person = self.humans.pop(0)
            for p in person.family:
                index = self.find_in_queue(p)
                if index is not None:
                    self.humans.pop(index)
            return person
        return None

    def get_next_blood_type(self, blood_type):
        for i, person in enumerate(self.humans):
            if person.blood_type == blood_type:
                for p in person.family:
                    index = self.find_in_queue(p)
                    if index is not None:
                        self.humans.pop(index)
                return self.humans.pop(i)
        return None

    def sort_by_age(self):
        self.humans = sorted(self.humans, key=lambda x: (-x.priority, x.age))
        self.humans.reverse()

    def rearrange_queue(self):
        new_queue = []
        families = {}
        for person in self.humans:
            if person.family:
                if person.family[0].id_number not in families:
                    families[person.family[0].id_number] = []
                families[person.family[0].id_number].append(person)
            else:
                new_queue.append(person)

        for family in families.values():
            for i in range(len(family)):
                if i == 0 or family[i-1].family[0].id_number != family[i].family[0].id_number:
                    new_queue.append(family[i])

        self.humans = new_queue
# create some humans
h1 = Human("1", "Alice", 40, False, "A")
h2 = Human("2", "Bob", 70, True, "B")
h3 = Human("3", "Charlie", 50, False, "AB")
h4 = Human("4", "David", 80, True, "O")
h5 = Human("5", "Eve", 30, False, "A")
h6 = Human("6", "Frank", 65, False, "B")
h7 = Human("7", "Grace", 75, False, "AB")
h8 = Human("8", "Henry", 55, False, "O")
h9 = Human("9", "Ivy", 20, True, "A")
h10 = Human("10", "John", 90, False, "B")

# add family members
h1.add_family_member(h2)
h1.add_family_member(h5)
h2.add_family_member(h1)
h3.add_family_member(h6)
h4.add_family_member(h7)
h5.add_family_member(h1)
h6.add_family_member(h3)
h7.add_family_member(h4)
h8.add_family_member(h9)
h9.add_family_member(h8)

# create a queue and add some people to it
q = Queue()
q.add_person(h3)
q.add_person(h2)
q.add_person(h5)
q.add_person(h7)
q.add_person(h1)
q.add_person(h4)
q.add_person(h6)
q.add_person(h9)
q.add_person(h10)
q.add_person(h8)

# sort the queue by age and print the order
q.sort_by_age()
for i, person in enumerate(q.humans):
    print(f"{i+1}. {person.name} ({person.age}) - priority: {person.priority}, blood type: {person.blood_type}, family: {[member.name for member in person.family]}")

# rearrange the queue so that family members are not adjacent and print the order
q.rearrange_queue()
for i, person in enumerate(q.humans):
    print(f"{i+1}. {person.name} ({person.age}) - priority: {person.priority}, blood type: {person.blood_type}, family: {[member.name for member in person.family]}")

# get the next person and print their name and family members
person = q.get_next()
print(f"Next person: {person.name} ({person.age}) - priority: {person.priority}, blood type: {person.blood_type}, family: {[member.name for member in person.family]}")

# get the next person with blood type A and print their name and family members
person = q.get_next_blood_type("A")
print(f"Next person with blood type A: {person.name} ({person.age}) - priority: {person.priority}, blood type: {person.blood_type}, family: {[member.name for member in person.family]}")
