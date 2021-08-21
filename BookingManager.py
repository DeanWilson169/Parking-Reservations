# from datetime import date
from datetime import date, timedelta
from Booking import Booking
class BookingManager:
    def determine24HourNotice(self, dateOfBooking):
        within24HoursFromToday = date.today() + timedelta(hours=24)
        if dateOfBooking >= within24HoursFromToday:
            return True
        else: 
            return False
    
    def occupyParkingBay(self, carpark, booking):
        availableParkingBay = booking.getParkingBayNumber()
        if availableParkingBay != 0:
            carpark.occupyAvailableParkingBay(availableParkingBay, booking)
        else:
            raise Exception('No available bays at time of booking')

    def createBooking(self, customer, dateOfBooking, carpark):
        isNotWithin24HoursOfBooking = self.determine24HourNotice(dateOfBooking)
        if isNotWithin24HoursOfBooking:
            booking = Booking(customer, dateOfBooking, carpark)
            customer.assignNewBooking(booking)
            self.occupyParkingBay(carpark, booking)
            return booking 
        else:
            raise Exception("Please book 24 hours in advance")

    def getBookingsFromDate(self, date, carpark):
        carparkBookings = carpark.getCarparkBookings()
        bookingsFromDate = []
        for booking in carparkBookings:
            if booking.dateOfBooking == date:
                bookingsFromDate.append(booking)
        return bookingsFromDate
