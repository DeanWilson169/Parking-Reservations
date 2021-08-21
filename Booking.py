from CarPark import CarPark
from datetime import date

class Booking:
    customerName = ''
    parkingBayNumber = 0
    dateOfBooking = date
    dateBookingWasMade = date.today()
    carpark = CarPark(0)

    def __init__(self, customerName, dateOfBooking, carpark):
        self.customerName = customerName
        self.dateOfBooking = dateOfBooking
        self.dateBookingWasMade = date.today()
        self.carpark = carpark
        self.parkingBayNumber = carpark.determineAvailableParkingBay()
    
