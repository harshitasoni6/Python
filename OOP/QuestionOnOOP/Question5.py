'''
# Question 1: Implementing a Vehicle Hierarchy

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Design a Python class named `Vehicle` to represent a generic vehicle.

    Theory:
    A vehicle is a machine that transports people or cargo from one place to another.

    Operations:
    1. Start: Start the vehicle's engine. (Abstract Method)
    2. Stop: Stop the vehicle's engine.
    3. Drive: Drive the vehicle.

    Test Cases:
    Test Case 1:
    vehicle = Car("Toyota", "Red")
    assert vehicle.start() == "Starting the Toyota engine"
    assert vehicle.stop() == "Stopping the Toyota engine"
    assert vehicle.drive() == "Driving the Toyota"

    Test Case 2:
    # Additional test cases can be added here
    pass


class Car(Vehicle):
    """
    Design a Python class named `Car` to represent a car.

    Theory:
    A car is a road vehicle typically with four wheels, powered by an internal combustion engine.

    Operations:
    1. Lock Doors: Lock the car's doors.
    2. Unlock Doors: Unlock the car's doors.

    Test Cases:
    Test Case 1:
    car = Car("Toyota", "Red")
    assert car.start() == "Starting the Toyota engine"
    assert car.lock_doors() == "Locking the Toyota doors"
    assert car.drive() == "Driving the Toyota"

    Test Case 2:
    # Additional test cases can be added here
    pass


class Bicycle(Vehicle):
    """
    Design a Python class named `Bicycle` to represent a bicycle.

    Theory:
    A bicycle is a human-powered or motor-powered vehicle with two wheels.

    Operations:
    1. Pedal: Move the bicycle forward by pedaling.
    2. Ring Bell: Ring the bicycle's bell.

    Test Cases:
    Test Case 1:
    bicycle = Bicycle("Mountain Bike", "Green")
    assert bicycle.start() == "Starting the Mountain Bike engine"
    assert bicycle.pedal() == "Moving forward by pedaling"
    assert bicycle.ring_bell() == "Ringing the bell"

    Test Case 2:
    # Additional test cases can be added here
    pass
    """
'''