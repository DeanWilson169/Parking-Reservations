class Carpark:
    
    def __init__(self, totalParkingBays):
        self.totalParkingBays = totalParkingBays
        self.carparkBookings = []   
        self.availableParkingBays = []
        for i in range(totalParkingBays):
            self.availableParkingBays.append(i+1)
        
    def getTotalParkingBays(self):
        return self.totalParkingBays

    def getAvailableParkingBays(self):
        return self.availableParkingBays

    def getCarparkBookings(self):
        return self.carparkBookings
    
    def occupyAvailableParkingBay(self, parkingBayNumber, booking):
        for bay in self.availableParkingBays:
            if parkingBayNumber == bay:
                self.availableParkingBays.remove(parkingBayNumber)
                self.carparkBookings.append(booking)

    def determineAvailableParkingBay(self):
        availableBays = self.getAvailableParkingBays()
        if len(availableBays) > 0:
            return availableBays[0]
        else:
            return 0