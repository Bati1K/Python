
class flight:
    
    def __init__(self, name, number, status):
        self.name = name 
        self.number = number
        self.status = status

flights = [
    flight("SouthWest", 793, "arrived"),
    flight("America AL", 139, "arrived"),
    flight("Turkish", 803, "in Route" )
]

#to sort student by grade.
flightResult = []
for flight in flights:
    if flight.status == "arrived":
        flightResult.append(f"{flight.name} Has Arrived")
    else: 
        flightResult.append(f"{flight.name} In Route")


# mapResult = list(map(lambda flight: flight.name, flights))
# print(mapResult)
flightStatusMap = {flight.number: flight.status for flight in flights}
direction = int(input("Enter flight number? "))
if direction in flightStatusMap:
    status = flightStatusMap[direction]
    print(f"{flight.name} Air Line {direction}: {status}")
else:
    print("Can not find flight")