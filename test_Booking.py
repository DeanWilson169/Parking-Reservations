from Carpark import Carpark
from Booking import Booking
from BookingManager import BookingManager
from Customer import Customer
from datetime import date
import pytest

class TestBooking:
    class TestGetCustomer:

        def test_getCustomer(self):
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            
            assert booking.getCustomer() == alice
    
    class TestGetParkingBayNumber:
       
        def test_getFirstParkingBayWhenThereIsOnlyOneBookingMade(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingDate = date(2022, 6, 1)
            bookingManager = BookingManager()
            
            alice = Customer("Alice", '1ABC123')
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            assert booking.getParkingBayNumber() == 1
        
        def test_getSecondParkingBayWhenThereIsABookingMadeForTheFirstBay(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingDate = date(2022, 6, 1)
            bookingManager = BookingManager()
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice, bookingDate, carpark)

            bob = Customer("Bob", '1DEF123')
            booking2 = bookingManager.createBooking(bob, bookingDate, carpark)

            assert booking2.getParkingBayNumber() == 2
    
    class TestGetDateOfBooking:
       
        def test_getDateOfBooking(self):
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4

            carpark = Carpark(numberOfParkingBays)

            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)

            assert booking.getDateOfBooking() == bookingDate

    class TestGetDateBookingWasMade:
        
        def test_getDateBookingWasMade(self):
            dateBookingWasMade = date.today()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4

            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            
            assert booking.getDateBookingWasMade() == dateBookingWasMade
    
    class TestCarparkBookingWasMadeFor:
        
        def test_getCarparkBookingWasMadeFor(self):
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4

            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            
            assert booking.getCarparkBookingWasMadeFor() == carpark
