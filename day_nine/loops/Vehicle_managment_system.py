#5. Vehicle Management System (Inheritance)
#A transport company manages different vehicles. Create a base class Vehicle with
#attributes like brand and speed. Create derived classes Car and Bike that inherit from
#Vehicle and display their details.


class vehicle :
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def display_detailes(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)



class car(vehicle):
    pass

class bike(vehicle):
    pass

car = car("toyota",200)
bike = bike("duke",150)

car.display_detailes()
bike.display_detailes()
