"""
Classes and objects

"""

class Myclass:
    pass

class Calculator:

    def __init__(self):
        pass

    def addition(self):
        print('Sum of two numbers')

    def substraction(self):
        print("Substraction")

    def mul(self):
        print('Multiplication')


obj = Calculator()
#
# print(obj.addition())
#
# print(obj.substraction())

####

class Person:

    def __init__(self, first_name, last_name, height, age, weight):
        self.first_name, self.last_name = first_name, last_name
        self.height = height
        self.age = age
        self.weight = weight


    def full_name(self):
        return 'My full name is {0} -- {1}'.format(self.first_name, self.last_name)

    def age_in_days(self):
        return "My age in days : {0}".format(self.age * 365)


object_one = Person(first_name='Sreeram', last_name='kalluri', height=6, age=25, weight=50)

print(object_one.first_name)
print(object_one.last_name)

print(object_one.full_name())
print(object_one.age_in_days())
##################################################################


object_two = Person(first_name='Sachin', last_name='Tendulkar', height=5.5, age=40, weight=60)

print(object_two.full_name())
print(object_two.age_in_days())

########################################

class Car:

    def __init__(self, model, company, color, size=0, made_in=2015):
        self.model = model
        self.company = company
        self.color = color

    def basic_conf(self):
        return "The car model name is :{0}- The company name is {1}- color:{2}".format(self.model, self.company, self.color)



benz_object = Car(model='New', company='X company', color='red')

print(benz_object.basic_conf())