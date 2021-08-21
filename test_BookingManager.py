from datetime import date, timedelta

import pytest

from Booking import Booking
from BookingManager import BookingManager
from Carpark import Carpark
from Customer import Customer
class TestBookingManager:
    class TestDetermine24HourNotice:

        def test_bookingMadeWithMoreThan24HoursNotice(self):
            bookingDateTime = date.today() + timedelta(hours=50)
            bookingManager = BookingManager()
            assert bookingManager.determine24HourNotice(bookingDateTime) == True

        def test_bookingMadeWith23HoursNotice(self):    
            bookingDateTime = date.today() + timedelta(hours=23)
            bookingManager = BookingManager()
            assert bookingManager.determine24HourNotice(bookingDateTime) == False

        def test_bookingMadeWith24HoursNotice(self):    
            bookingDateTime = date.today() + timedelta(hours=24)
            bookingManager = BookingManager()
            assert bookingManager.determine24HourNotice(bookingDateTime) == True
        
        def test_bookingMadeWith25HoursNotice(self):    
            bookingDateTime = date.today() + timedelta(hours=25)
            bookingManager = BookingManager()
            assert bookingManager.determine24HourNotice(bookingDateTime) == True

        def test_bookingMadeWith0HoursNotice(self):    
            bookingDateTime = date.today()
            bookingManager = BookingManager()
            assert bookingManager.determine24HourNotice(bookingDateTime) == False
    class TestOccupyParkingBay:

        def test_Occupy1BayIfNoBaysAreCurrentlyOccupied(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)

            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking)
            
            assert carpark.getAvailableParkingBays() == [2,3,4]

        def test_Occupy2BaysIf1BayIsCurrentlyOccupied(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)

            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking)

            bob = Customer("Bob", '1DEF123')
            booking2 = Booking(bob, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking2)

            assert carpark.getAvailableParkingBays() == [3,4]

        def test_Occupy3BaysIf2BaysAreCurrentlyOccupied(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)

            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking)

            bob = Customer("Bob", '1DEF123')
            booking2 = Booking(bob, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking2)

            charlie = Customer("Charlie", '1GHI123')
            booking3 = Booking(charlie, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking3)

            assert carpark.getAvailableParkingBays() == [4]

        def test_Occupy4BaysIf3BaysAreCurrentlyOccupied(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking)
            
            bob = Customer("Bob", '1DEF123')
            booking2 = Booking(bob, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking2)
            
            charlie = Customer("Charlie", '1GHI123')
            booking3 = Booking(charlie, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking3)
            
            dave = Customer("Dave", '1JKL123')
            booking4 = Booking(dave, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking4)

            assert carpark.getAvailableParkingBays() == []

        def test_ThrowExceptionIfAllBaysAreCurrentlyOccupied(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)

            alice = Customer("Alice", '1ABC123')
            booking = Booking(alice, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking)
            
            bob = Customer("Bob", '1DEF123')
            booking2 = Booking(bob, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking2)
            
            charlie = Customer("Charlie", '1GHI123')
            booking3 = Booking(charlie, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking3)
            
            dave = Customer("Dave", '1JKL123')
            booking4 = Booking(dave, bookingDate, carpark)
            bookingManager.occupyParkingBay(carpark, booking4)

            ed = Customer("Ed", '1MNO123')
            booking5 = Booking(dave, bookingDate, carpark)
            with pytest.raises(Exception):
                bookingManager.occupyParkingBay(carpark, booking5)

    class TestCreateBooking:
        def test_successfulBookingMade(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()

            alice = Customer("Alice", '1ABC123')
            bookingDate = date(2022, 6, 1)
            booking = bookingManager.createBooking(alice, bookingDate, carpark)

            assert type(booking) == Booking
        
        def test_successfulBookingMadeOnASeperateDay(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()

            alice = Customer("Alice", '1ABC123')
            bookingDate = date(2022, 6, 1)
            bookingManager.createBooking(alice, bookingDate, carpark)

            ed = Customer("Ed", '1MNO123')
            bookingDate = date(2022, 6, 2)
            booking2 = bookingManager.createBooking(ed, bookingDate, carpark)

            assert type(booking2) == Booking
        
        def test_successfulBookingMadeWhenThereAre3RemainingParkingBays(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)

            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice,bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            booking = bookingManager.createBooking(bob,bookingDate, carpark)
            
            assert type(booking) == Booking

        def test_successfulBookingMadeWhenThereAre2RemainingParkingBays(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice,bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingManager.createBooking(bob,bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            booking = bookingManager.createBooking(charlie,bookingDate, carpark)
            
            assert type(booking) == Booking

        def test_successfulBookingMadeWhenThereIs1RemainingParkingBay(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingDate = date(2022, 6, 1)
            bookingManager = BookingManager()
            
            alice = Customer("Alice", '1ABC123')
            bookingManager.createBooking(alice,bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingManager.createBooking(bob,bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            bookingManager.createBooking(charlie,bookingDate, carpark)
            
            dave = Customer("Dave", '1JKL123')
            booking = bookingManager.createBooking(dave,bookingDate, carpark)
            
            assert type(booking) == Booking
        
        def test_unsuccessfulBookingWhenIsFull(self):
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()
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
                bookingManager.createBooking(ed,bookingDate, carpark)

    class TestGetBookingsFromDate:

        def test_GetNoBookingsWhenNoBookingsAreMadeOnTheGivenDate(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == []
        
        def test_Get1BookingWhenASingleBookingIsMadeOnTheGivenDate(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == [booking]

        def test_Get2BookingsWhen2BookingsAreMadeOnTheGivenDate(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            booking2 = bookingManager.createBooking(bob, bookingDate, carpark)


            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == [booking, booking2]

        def test_Get3BookingsWhen3BookingsAreMadeOnTheGivenDate(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            booking2 = bookingManager.createBooking(bob, bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            booking3 = bookingManager.createBooking(charlie, bookingDate, carpark)
            
            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == [booking, booking2, booking3]
        
        def test_Get4BookingsWhen4BookingsAreMadeOnTheGivenDate(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            booking2 = bookingManager.createBooking(bob, bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            booking3 = bookingManager.createBooking(charlie, bookingDate, carpark)
            
            dave = Customer("Dave", '1JKL123')
            booking4 = bookingManager.createBooking(dave, bookingDate, carpark)
            
            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == [booking, booking2, booking3, booking4]
        
        def test_OnlyGetThe4ValidBookingsAfter5BookingsHaveAttemptedToBeMadeOnTheGivenDate(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", '1ABC123')
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            booking2 = bookingManager.createBooking(bob, bookingDate, carpark)
            
            charlie = Customer("Charlie", '1GHI123')
            booking3 = bookingManager.createBooking(charlie, bookingDate, carpark)
            
            dave = Customer("Dave", '1JKL123')
            booking4 = bookingManager.createBooking(dave, bookingDate, carpark)
            
            ed = Customer("Ed", '1MNO123')
            with pytest.raises(Exception):
                booking4 = bookingManager.createBooking(ed, bookingDate, carpark)
            
            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == [booking, booking2, booking3, booking4]

        def test_Get1BookingWhen2BookingsAreMadeOnSeperateDates(self):
            bookingManager = BookingManager()
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)

            alice = Customer("Alice", '1ABC123')
            bookingDate = date(2022, 6, 1)
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            bob = Customer("Bob", '1DEF123')
            bookingDate2 = date(2022, 6, 2)
            bookingManager.createBooking(bob, bookingDate2, carpark)
            
            assert bookingManager.getBookingsFromDate(bookingDate, carpark) == [booking]
