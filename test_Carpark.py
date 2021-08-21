from CarPark import CarPark
from BookingManager import BookingManager
from datetime import date

class TestCarPark:

    def test_getAvailableParkingBays(self):
        carpark = CarPark(4)
        assert carpark.getAvailableParkingBays() == [1,2,3,4]

    def test_occupyAvailableParkingBay(self):
        parkingBayNumber = 3
        carpark = CarPark(4)
        carpark.occupyAvailableParkingBay(parkingBayNumber)
        carpark.getAvailableParkingBays() == [1,2,4]

    class TestDetermineAvailableParkingBays:
        def test_returnParkingBay1WhenNoBaysAreBooked(self):
            carpark = CarPark(4)
            assert carpark.determineAvailableParkingBay() == 1

        def test_returnParkingBay2WhenBay1IsBooked(self):
            carpark = CarPark(4)
            bookingDate = date(2022, 6, 1)
            BookingManager.createBooking(self, "Alice", bookingDate, carpark)
            assert carpark.determineAvailableParkingBay() == 2

        def test_returnParkingBay3WhenBay1And2AreBooked(self):
            carpark = CarPark(4)
            bookingDate = date(2022, 6, 1)
            BookingManager.createBooking(self, "Alice", bookingDate, carpark)
            BookingManager.createBooking(self, "Bob", bookingDate, carpark)
            assert carpark.determineAvailableParkingBay() == 3
        
        def test_returnParkingBay4WhenBayAllOtherBaysAreBooked(self):
            carpark = CarPark(4)
            bookingDate = date(2022, 6, 1)
            BookingManager.createBooking(self, "Alice", bookingDate, carpark)
            BookingManager.createBooking(self, "Bob", bookingDate, carpark)
            BookingManager.createBooking(self, "Charlie", bookingDate, carpark)
            assert carpark.determineAvailableParkingBay() == 4
        
        def test_return0WhenBayAllBaysAreBookedOut(self):
            carpark = CarPark(4)
            bookingDate = date(2022, 6, 1)
            BookingManager.createBooking(self, "Alice", bookingDate, carpark)
            BookingManager.createBooking(self, "Bob", bookingDate, carpark)
            BookingManager.createBooking(self, "Charlie", bookingDate, carpark)
            BookingManager.createBooking(self, "Dave", bookingDate, carpark)
            assert carpark.determineAvailableParkingBay() == 0
        
        def test_return0WhenBayAllBaysAreBookedOutAndAnotherBookingIsAttemptedToBeMade(self):
            carpark = CarPark(4)
            bookingDate = date(2022, 6, 1)
            BookingManager.createBooking(self, "Alice", bookingDate, carpark)
            BookingManager.createBooking(self, "Bob", bookingDate, carpark)
            BookingManager.createBooking(self, "Charlie", bookingDate, carpark)
            BookingManager.createBooking(self, "Dave", bookingDate, carpark)
            BookingManager.createBooking(self, "Ed", bookingDate, carpark)
            assert carpark.determineAvailableParkingBay() == 0