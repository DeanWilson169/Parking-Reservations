# Running Tests

1. install pytest with the following command:

'''md
    pip install -U pytest
'''
2. Check that you installed the correct version

'''md
    $ pytest --version
    pytest 6.2.4
'''

3. Run the following command to run all tests

'''md
    pytest
'''

# Assumptions

- The date for the booking comes from somewhere else, e.g. user input

# Design Decisions

I wanted to tackle this in a Object Oriented Programming paradigm as I have more experience with Functional Programming in JavaScript but I thought the task requirements made more sense in an OOP structure.

Customer:

Acts as a record for each Customer making a booking

Booking:

Stores the necessary information for an individual booking for a specific customer on a specific day at a specific carpark

Carpark:

Stores and manages the necessary data to calculate how many parking bays are available on a given day

BookingManager:

Brings all the components together. Handles the creation of bookings, can retrieve bookings from a given date, etc

# Trade-offs

I don't believe I made any!

# Note

Thanks for taking the time to look at my work.

- Dean Wilson