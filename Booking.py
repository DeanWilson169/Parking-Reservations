from datetime import date

class Booking:

    def __init__(self, customer, dateOfBooking, carpark):
        self.customer = customer
        self.dateOfBooking = dateOfBooking
        self.dateBookingWasMade = date.today()
        self.carpark = carpark
        self.parkingBayNumber = carpark.determineAvailableParkingBay()

    def getCustomer(self):
        return self.customer

    def getParkingBayNumber(self):
        return self.parkingBayNumber
    
    def getDateOfBooking(self):
        return self.dateOfBooking

    def getDateBookingWasMade(self):
        return self.dateBookingWasMade

    def getCarparkBookingWasMadeFor(self):
        return self.carpark