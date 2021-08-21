class Customer:

    def __init__(self, name, licencePlate):
        self.name = name
        self.licencePlate = licencePlate
        self.customerBookings = []
        
    def getCustomerName(self):
        return self.name
    
    def getCustomerLicencePlate(self):
        return self.licencePlate

    def getCustomerBookings(self):
        return self.customerBookings

    def getCustomerRecord(self):
        return [self.name, self.licencePlate]

    def assignNewBooking(self, booking):
        if len(self.customerBookings) > 0:
            for customerBooking in self.customerBookings:
                if customerBooking.dateOfBooking != booking.dateOfBooking:
                    break
                else:
                    raise Exception('Customer has already made booking for this day')
        self.customerBookings.append(booking)