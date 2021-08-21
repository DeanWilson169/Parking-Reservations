from Customer import Customer
from Booking import Booking
from BookingManager import BookingManager
from Carpark import Carpark
from datetime import date
import pytest

class TestCustomer:
    class TestGetCustomerName:
        def test_getCustomerName(self):
            alice = Customer("Alice", "1ABC123")
            assert alice.getCustomerName() == "Alice"

    class TestGetCustomerLicencePlate:
        def test_getCustomerLicencePlate(self):
            alice = Customer("Alice", "1ABC123")
            assert alice.getCustomerLicencePlate() == "1ABC123"
    
    class TestGetCustomerBookings:
        def test_getOneBookingIfTheCustomerHasOnlyMadeASingleBooking(self):
            bookingManager = BookingManager()
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            
            alice = Customer("Alice", "1ABC123")
            booking = bookingManager.createBooking(alice, bookingDate, carpark)
            
            assert alice.getCustomerBookings() == [booking]
        
        def test_getTwoBookingIfTheCustomerHasMadeTwoBookingsOnDifferentDays(self):
            alice = Customer("Alice", "1ABC123")
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
            bookingManager = BookingManager()

            bookingDate = date(2022, 6, 1)
            booking = bookingManager.createBooking(alice, bookingDate, carpark)

            bookingDate2 = date(2022, 6, 2)
            booking2 = bookingManager.createBooking(alice, bookingDate2, carpark)
            
            assert alice.getCustomerBookings() == [booking, booking2]

    class TestGetCustomerRecord:
        def test_getCustomerRecord(self):
            alice = Customer("Alice", "1ABC123")
            assert alice.getCustomerRecord() == ["Alice", "1ABC123"]

    class TestAssignNewBooking:
        def test_customerMakesSuccessfulBooking(self):
            customer = Customer( 'Alice', '1ABC123')
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)            
            
            booking = Booking(customer.name, bookingDate, carpark)
            customer.assignNewBooking(booking)
            
            assert customer.getCustomerBookings() == [booking]
        
        def test_customerMakes2BookingsOnDifferentDays(self):
            customer = Customer( 'Alice', '1ABC123')
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)
          
            bookingDate = date(2022, 6, 1)
            booking = Booking(customer.name, bookingDate, carpark)
            customer.assignNewBooking(booking)

            bookingDate2 = date(2022, 6, 2)
            booking2 = Booking(customer.name, bookingDate2, carpark)
            customer.assignNewBooking(booking2)
            
            assert customer.getCustomerBookings() == [booking, booking2]

        def test_ThrowExceptionIfCustomerTriesToMakeAnotherBookingOnSameDay(self):
            customer = Customer( 'Alice', '1ABC123')
            bookingDate = date(2022, 6, 1)
            numberOfParkingBays = 4
            carpark = Carpark(numberOfParkingBays)            
            
            booking = Booking(customer.name, bookingDate, carpark)
            customer.assignNewBooking(booking)
            
            booking2 = Booking(customer.name, bookingDate, carpark)
            with pytest.raises(Exception):
                customer.assignNewBooking(booking2)
            
            assert customer.getCustomerBookings() == [booking]
