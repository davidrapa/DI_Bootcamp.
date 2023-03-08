# Instructions : Air Management System
# Your goal is to build an airplanes traffic management system.
#
#
#
# Details
# Your program should rely on four classes: Airline, Airplane, Flight and Airport.
#
# Consider every plane can fly only once per day.
#
#
#
# The Airline Class
# Attributes:
#
# id (str) A two letters code
# name (str)
# planes : A list of Airplanes belonging to this airline (see below the Airplane class)
# This class has no methods
#
#
#
# The Airplane Class
# Attributes:
#
# id (int)
# current_location : The Airport where the airplane is currently located (see below the Airport class)
# company : The airline this airplane belongs to (see above the Airline class)
# next_flights : The list of Flights. Every future flights of the airplane, this list should always be sorted by datetime. (see below the Flight class)
#
#
# Methods:
#
# fly(self, destination)
# location_on_date(self, date): Returns where the plane will be on this date
# available_on_date(self, date, location) : Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).
#
#
# The Flight Class
# Attributes:
#
# date (datetime.Date)
# destination : The destination airport. (see below the Airport class)
# origin : The departure airport. (see below the Airport class)
# plane : The plane used during this flight. (see above the Airplane class)
# id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.
# Methods:
#
# Those methods are here only to update the rest of the system, for example, to change the location of the plane when it reaches its destination:
#
# take_off(self)
# land(self)
#
#
# The Airport Class
# Attributes:
#
# city (str) The code of the city where the airport is located
# planes : The list of every plane that is currently in this airport. (see above the Airplane class)
# scheduled_departures : The list of flight - Every future flight from this airport, sorted by date. (see above the Flight class)
# scheduled_arrivals : The list of flight - Every future flight that will arrive to this airport, sorted by date. (see above the Flight class)
#
#
# Methods:
#
# schedule_flight(self, destination, datetime) :
# finds an available airplane from an airline, that serves the departure and the destination
# schedule the airplane for the flight
# info(self, start_date, end_date) : Displays every scheduled flight from start_date to end_date.
#
#
# You are free to add any class/method/attribute to your code, be sure to document everything you write.
#
# Write a small code to test your program.

import datetime

class Airline:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.planes = []

    def add_plane(self, plane):
        self.planes.append(plane)


class Airplane:
    def __init__(self, id, current_location, company):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []

    def available_on_date(self, date, airport):
        if self.current_location != airport:
            return False
        for flight in self.next_flights:
            if flight.date == date:
                return False
        return True


class Flight:
    def __init__(self, date, destination, origin, plane):
        self.id = str(len(destination.scheduled_arrivals))
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane

    def take_off(self):
        self.plane.current_location = None

    def land(self):
        self.plane.current_location = self.destination
        self.destination.planes.append(self.plane)


class Airport:
    def __init__(self, code, city, gates, terminals):
        self.code = code
        self.city = city
        self.gates = gates
        self.terminals = terminals
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            if plane.company.planes.count(plane) > 0 and plane.available_on_date(datetime.date(), self):
                flight = Flight(datetime.date(), destination, self, plane)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
                plane.next_flights.append(flight)
                break

    def info(self, start_date, end_date):
        print(f"Upcoming flights from {self.city}:\n")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"Flight ID: {flight.id}, Departure: {flight.origin.code}, Destination: {flight.destination.code}, Date: {flight.date}")
        print("\n")
        print(f"Upcoming flights to {self.city}:\n")
        for flight in self.scheduled_arrivals:
            if start_date <= flight.date <= end_date:
                print(f"Flight ID: {flight.id}, Departure: {flight.origin.code}, Destination: {flight.destination.code}, Date: {flight.date}")

# create airports
jfk = Airport("JFK", "New York", 1, 2)
cdg = Airport("CDG", "Paris", 1, 2)

# create airlines
aa = Airline("AA", "American Airlines")
af = Airline("AF", "Air France")

# create planes
aa_p1 = Airplane(1, jfk, aa)
af_p1 = Airplane(2, cdg, af)

# schedule flights
jfk.schedule_flight(cdg, datetime.date(2023, 3, 7))
jfk.schedule_flight(cdg, datetime.date(2023, 3, 8))

# display scheduled flights
jfk.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))
cdg.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))


# display scheduled flights again
jfk.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))
cdg.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))

# land
# cdg.scheduled_arrivals[0].land()

# display scheduled flights again
jfk.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))
cdg.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))


print(jfk.scheduled_departures)
print(jfk.scheduled_arrivals)
print(cdg.scheduled_departures)
print(cdg.scheduled_arrivals)