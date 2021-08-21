# from datetime import date
from datetime import date
from CarPark import CarPark
from Booking import Booking

class BookingManager:

    date = None
    carpark = CarPark(0)

    def __init__(self, date):
        self.date = date
        self.carpark = CarPark(4)


    def createBooking(self, customer, dateofBooking, carpark):
        availableParkingBay = carpark.determineAvailableParkingBay()
        if availableParkingBay != 0:
            carpark.occupyAvailableParkingBay(availableParkingBay)
        else:
            raise Exception('No available bays at time of booking')
        booking = Booking(customer, dateofBooking, carpark)
        # Probably going to be it's own function
        customer.assignNewBooking(Booking)
        return booking


    # months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # thirtyOneDayMonths = [1,3,5,7,8,10,12]
    # thirtyDayMonths = [4,6,9,11]
    # day = []

    # # Indexed by Month, Day
    # occupied = [[[]]] 

    # def __init__(self):
    #     occupied = [[[]]] 
    #     for month in self.months:
    #         for i in self.thirtyOneDayMonths: 
    #             if month == i:
    #                 for day in range(31):
    #                     self.day[day] = day + 1
    #                     print(self.day[day])
        

    # def isLeapYear(year):
    #     if year % 4 == 0:
    #         if year % 100 == 0:
    #             if year % 400 == 0:
    #                 return True
    #             return False
    #         return True
    #     return False
        