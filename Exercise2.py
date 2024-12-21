class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Bike(Vehicle):
    def move(self):
        print("The bike is cycling on the trail.")

        vehicle = Vehicle()
car = Car()
bike = Bike()