"""
    Topic:  Class - Inheritance
    Author: YSK-PYTHON
    python : 3.5.2

"""

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def no_of_wheels(self):
        return "FOUR"


    def model_name(self):
        return self.name + '--' + self.price

my_car = Car(name='Audi', price='5B')

print(my_car.model_name())




class RedCar(Car):
    def __init__(self, name, price):
        super().__init__(name, price)

    def no_of_wheels(self):
        return 'Six wheels'





red_car = RedCar(name='Redcar', price='6B')
# print(red_car)
print(red_car.model_name())

print(red_car.no_of_wheels())