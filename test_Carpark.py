from Carpark import Carpark
from Booking import Booking
from BookingManager import BookingManager
from Customer import Customer
import pytest
from datetime import date

class TestCarpark:
    class TestGetTotalParkingBays:
        def test_getTotalParkingBays(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            assert carpark.getTotalParkingBays() == 4

    class TestGetAvailableParkingBays:
        def test_getAvailableParkingBays(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            assert carpark.getAvailableParkingBays() == [1,2,3,4]

    class TestGetCarparkBookings:
        def test_getTotalParkingBays(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            assert carpark.getTotalParkingBays() == 4

    class TestOccupyAvailableParkingBays:
        def test_occupyAvailableParkingBay(self):
            numberOfParkingBays = 4
            parkingBayNumber = 3
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            bookingDate = date(2022, 6, 1)
            booking = Booking(alice, bookingDate, carpark)

            carpark.occupyAvailableParkingBay(parkingBayNumber, booking)
            assert carpark.getAvailableParkingBays() == [1,2,4]

    class TestDetermineAvailableParkingBays:
        def test_returnParkingBay1WhenNoBaysAreBooked(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            assert carpark.determineAvailableParkingBay() == 1

        def test_returnParkingBay2WhenBay1IsBooked(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice, bookingDate, carpark)
            
            assert carpark.determineAvailableParkingBay() == 2

        def test_returnParkingBay3WhenBay1And2AreBooked(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingManager.createBooking(bob, bookingDate, carpark)
            
            assert carpark.determineAvailableParkingBay() == 3
        
        def test_returnParkingBay4WhenBayAllOtherBaysAreBooked(self):
            numberOfParkingBays = 4
            bookingManager = BookingManager()
            carpark = Carpark(numberOfParkingBays)
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingManager.createBooking(bob, bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            bookingManager.createBooking(charlie, bookingDate, carpark)
            
            assert carpark.determineAvailableParkingBay() == 4
        
        def test_return0BaysWhenAllBaysAreBookedOut(self):
            numberOfParkingBays = 4
            bookingManager = BookingManager()
            carpark = Carpark(numberOfParkingBays)
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingManager.createBooking(bob, bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            bookingManager.createBooking(charlie, bookingDate, carpark)
            
            dave = Customer("Dave", '1JKL123')
            bookingManager.createBooking(dave, bookingDate, carpark)
            
            assert carpark.determineAvailableParkingBay() == 0
        
        def test_return0BaysWhenAllBaysAreBookedOutAndAnotherBookingIsAttemptedToBeMade(self):
            numberOfParkingBays = 4
            bookingManager = BookingManager()
            carpark = Carpark(numberOfParkingBays)
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingManager.createBooking(bob, bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            bookingManager.createBooking(charlie, bookingDate, carpark)
            
            dave = Customer("Dave", '1JKL123')
            bookingManager.createBooking(dave, bookingDate, carpark)
            
            ed = Customer("Ed", '1MNO123')
            with pytest.raises(Exception):
                bookingManager.createBooking(ed, bookingDate, carpark)
            
            assert carpark.determineAvailableParkingBay() == 0