from Customer import Customer
from Booking import Booking
from CarPark import CarPark
from datetime import date
import pytest

class TestCustomer:

    class TestAssignNewBooking:

        def test_customerMakesSuccessfulBooking(self):
            customer = Customer( 'Alice', '1ABC123')
            bookingDate = date(2022, 6, 1)
            carpark = CarPark(4)            
            booking = Booking(customer.name, bookingDate, carpark)
            customer.assignNewBooking(booking)
            assert customer.getCustomerBookings() == [booking]