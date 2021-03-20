class Transport:

    def __init__(self, number, type_, velocity):
        self.number = number
        self.type = type_
        self.velocity = velocity   

    def finish(self, m, t):
        path = self.velocity * t        
        balance = path % m         
        distance = m-balance
        return distance  

class EngineTransport(Transport):

    def __init__(self, number, type_, velocity, oil_type):
        self.oil_distr = {'98': 1, '95': 0.9, '92': 0.8}
        if type_ == 2:
            self.oil_distr['95'] = 0.8
            self.oil_distr['92'] = 0.6
        velocity *= self.oil_distr[oil_type]
        super().__init__(number,type_, velocity)
        self.oil_type = oil_type 

with open('input.txt', 'r') as file:    
    race_config = file.readlines()
map_config = race_config[0].split()
vehicles = []
results = []
for i in range(1, len(race_config)):
    vehicle_config = race_config[i].split()
    if len(vehicle_config) == 3:    
        vehicle = Transport(vehicle_config[0], vehicle_config[1], vehicle_config[2])     
        vehicles.append(vehicle)
        
    else:
        vehicles.append(EngineTransport(vehicle_config[0], vehicle_config[1], vehicle_config[2], vehicle_config[3]))

print(min(vehicles[results[min(results)]]))





