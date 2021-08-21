from CarPark import CarPark
from BookingManager import BookingManager
from CarPark import CarPark
from Booking import Booking
from Customer import Customer
from datetime import date
import pytest

class TestBookingManager:

    class TestCreateBooking:

        alice = Customer("self.alice", '1ABC123')
        bob = Customer("Bob", '1DEF123')
        charlie = Customer("Charlie", '1GHI123')
        dave = Customer("Dave", '1JKL123')
        ed = Customer("Ed", '1MNO123')
        bookingDate = date(2022, 6, 1)
        carpark = CarPark(4)

        def test_successfulBookingMade(self):
            self.alice = Customer("self.alice", '1ABC123')
            bookingDate = date(2022, 6, 1)
            booking = BookingManager.createBooking(self, self.alice, bookingDate, self.carpark)
            assert type(booking) == Booking
        
        def test_successfulBookingMadeWhenThereAre3RemainingParkingBays(self):
            BookingManager.createBooking(self,self.alice,self.bookingDate, self.carpark)
            booking = BookingManager.createBooking(self,self.bob,self.bookingDate, self.carpark)
            assert type(booking) == Booking

        def test_successfulBookingMadeWhenThereAre2RemainingParkingBays(self):
            BookingManager.createBooking(self,self.alice,self.bookingDate, self.carpark)
            BookingManager.createBooking(self,self.bob,self.bookingDate, self.carpark)
            booking = BookingManager.createBooking(self,self.charlie,self.bookingDate, self.carpark)
            assert type(booking) == Booking

        def test_successfulBookingMadeWhenThereIs1RemainingParkingBay(self):
            BookingManager.createBooking(self,self.alice,self.bookingDate, self.carpark)
            BookingManager.createBooking(self,self.bob,self.bookingDate, self.carpark)
            BookingManager.createBooking(self,self.charlie,self.bookingDate, self.carpark)
            booking = BookingManager.createBooking(self,self.dave,self.bookingDate, self.carpark)
            assert type(booking) == Booking
        
        def test_unsuccessfulBookingWhenIsFull(self):
            BookingManager.createBooking(self, self.alice, self.bookingDate, self.carpark)
            BookingManager.createBooking(self, self.bob, self.bookingDate, self.carpark)
            BookingManager.createBooking(self, self.charlie, self.bookingDate, self.carpark)
            BookingManager.createBooking(self, self.dave, self.bookingDate, self.carpark)
            with pytest.raises(Exception):
                BookingManager.createBooking(self,self.ed,self.bookingDate, self.carpark)

    # def func(self, x):
    #     return x + 1

    # # def test_answer_fails():
    # #     assert func(3) == 5

    # def test_answer_passes(self):
    #     assert self.func(3) == 4



    # months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # thirtyOneDayMonths = [1,3,5,7,8,10,12]
    # thirtyDayMonths = [4,6,9,11]
    # day = [None]*31

    # def setupCalendar(self):
    #     occupied = [[[None]]]*365
    #     for booking in occupied:
    #         for month in self.months:
    #             for i in self.thirtyOneDayMonths:
    #                 if self.months.index(month) == i:
    #                     for day in range(31):
    #                         booking[month[self.day[day]]] = day + 1
    #                         print(booking[month[self.day[day]]])
    #     return False

    # def test_setupCalendar(self):
    #     assert self.setupCalendar() == False
        


    # class TestIsLeapYear():
    #     def test_is2000ALeapYear(self):
    #         year = 2000
    #         assert Calendar.isLeapYear(year) == True

    #     def test_is2020ALeapYear(self):
    #         year = 2020
    #         assert Calendar.isLeapYear(year) == True

    #     def test_is2021ALeapYear(self):
    #         year = 2021
    #         assert Calendar.isLeapYear(year) == False

    #     def test_is2022ALeapYear(self):
    #         year = 2022
    #         assert Calendar.isLeapYear(year) == False

    #     def test_is2023ALeapYear(self):
    #         year = 2023
    #         assert Calendar.isLeapYear(year) == False

    #     def test_is2024ALeapYear(self):
    #         year = 2024
    #         assert Calendar.isLeapYear(year) == True

