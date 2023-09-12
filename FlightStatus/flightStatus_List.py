
class flight:
    
    def __init__(self, name, number, status):
        self.name = name 
        self.number = number
        self.status = status

    def __repr__(self):
        return f"{self.name}: {self.status}"

flights = [
    flight("SouthWest", 793, "arrived"),
    flight("America AL", 139, "arrived"),
    flight("Turkish", 803, "in Route" ),
    flight("Air France", 456, "in Route"),
    flight("Lufthansa", 712, "arrived"),
    flight("Emirates", 999, "in Route"),
    flight("British Airways", 234, "arrived"),
    flight("Delta Airlines", 567, "in Route"),
    flight("Qatar Airways", 888, "arrived"),
]


arrivedFlights = []
for flight in flights:
    if flight.status == "arrived":
        arrivedFlights.append(flight)

filterList = list(filter(lambda flight: flight.status == "arrived", flights))

print("")

print(filterList)

print("")
