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



# display scheduled flights again
jfk.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))
cdg.info(datetime.date(2023, 3, 6), datetime.date(2023, 3, 10))


print(jfk.scheduled_departures)
print(jfk.scheduled_arrivals)
print(cdg.scheduled_departures)
print(cdg.scheduled_arrivals)