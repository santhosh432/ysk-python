"""
    Topic:  Class - Methods
    Author: YSK-PYTHON
    python : 3.5.2

"""


class Person:
    """ Person class """
    def normal_method(self):
        return 'Normal method', self

    @classmethod
    def class_method(cls):
        return 'Class Method', cls

    @staticmethod
    def static_method():
        return 'Static method'

obj = Person()

print(obj.normal_method())



print(obj.class_method())

print(Person.class_method())



print(obj.static_method())
#
print(Person.static_method())

###

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def person_details(self):
        return self.name + str(self.age)

    @staticmethod
    def person_mobile(mobile):
        return 'Mobile number: {0}'.format(mobile)

    @staticmethod
    def person_basic_details():
        return 'Person is good'

    @staticmethod
    def person_info(mobile_no):
        return "Person has two legs , two eyes , one nose etc...........{0}".format(mobile_no)



p = Person(name='sree', age=25)
print(p.person_info(456456455656))
print(p.person_details())

print(p.person_mobile('84456456446'))

print(p.person_basic_details())

class Sizes:
    def __init__(self):
        pass

    def general(self, r):
        return self.area_of_circle(r)

    @staticmethod
    def area_of_circle(r, pi=3.14):
        return pi * r * r

    @staticmethod
    def area_of_square(s):
        return 4 * s

print(Sizes.area_of_square(s=4))



print(Sizes.area_of_circle(r=5))

obj2 = Sizes()

print(obj2.general(8))