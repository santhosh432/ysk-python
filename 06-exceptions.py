

# Exception: run time errors:

# print(2/

a = 2
b = 0

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print(' 0 cant be divided')


try:
    fullname = 'sreeram' + last_name
    print(fullname)
except NameError:
    print('Invalid code')

try:
    d = '2' + 6
    print(d)
except TypeError:
    print('Invalid format of integers')


def sum(a, b):

    try:
        total = '5' + two
        c = a + b
        print(c)
    except (TypeError, NameError):
        print("Please specify valid format ")


def div(a, b):
    try:
        c= a/b
        return c
    except ZeroDivisionError:
        print('Please specify b must be greater than zero ')

# print(div(5, 0))


print(sum('5',3))