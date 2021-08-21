from datetime import datetime


class CarPark:
    totalParkingBays = 0
    availableParkingBays = []

    def __init__(self, totalParkingBays):
        self.totalParkingBays = totalParkingBays
        self.availableParkingBays = [None]*totalParkingBays
        for i in range(totalParkingBays):
            self.availableParkingBays[i] = i+1
        
    def getTotalParkingBays(self):
        return self.totalParkingBays

    def getAvailableParkingBays(self):
        return self.availableParkingBays
    
    def occupyAvailableParkingBay(self, parkingBayNumber):
        for bay in self.availableParkingBays:
            if parkingBayNumber == bay:
                self.availableParkingBays.remove(parkingBayNumber)

    def determineAvailableParkingBay(self):
        availableBays = self.getAvailableParkingBays()
        if len(availableBays) > 0:
            return availableBays[0]
        else:
            return 0