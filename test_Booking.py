from CarPark import CarPark
from Booking import Booking
from CarPark import CarPark
import pytest

class TestBooking:

    class TestCreateBooking:
        def test_successfulBookingMade(self):
            carpark = CarPark(4)
            booking = Booking.createBooking(self,'Alice','010121', carpark)
            assert type(booking) == Booking
        
        def test_successfulBookingMadeWhenThereAre3RemainingParkingBays(self):
            carpark = CarPark(4)
            Booking.createBooking(self,'Alice','010121', carpark)
            booking = Booking.createBooking(self,'Bob','010121', carpark)
            assert type(booking) == Booking

        def test_successfulBookingMadeWhenThereAre2RemainingParkingBays(self):
            carpark = CarPark(4)
            Booking.createBooking(self,'Alice','010121', carpark)
            Booking.createBooking(self,'Bob','010121', carpark)
            booking = Booking.createBooking(self,'Charlie','010121', carpark)
            assert type(booking) == Booking

        def test_successfulBookingMadeWhenThereIs1RemainingParkingBay(self):
            carpark = CarPark(4)
            Booking.createBooking(self,'Alice','010121', carpark)
            Booking.createBooking(self,'Bob','010121', carpark)
            booking = Booking.createBooking(self,'Charlie','010121', carpark)
            assert type(booking) == Booking
        
        def test_unsuccessfulBookingWhenCarparkIsFull(self):
            carpark = CarPark(4)
            Booking.createBooking(self, "Alice", '010121', carpark)
            Booking.createBooking(self, "Bob", '010121', carpark)
            Booking.createBooking(self, "Charlie", '010121', carpark)
            Booking.createBooking(self, "Dave", '010121', carpark)
            with pytest.raises(Exception):
                Booking.createBooking(self,'Ed','010121', carpark)