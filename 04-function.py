

def full_name(first_name, age, mobile_no, last_name='My Last name', ):

    full_named = first_name + '--' + last_name

    return full_named



print(full_name(first_name='sreeram', age=20, mobile_no=455644446))

print(full_name(first_name='sachin', age=30, mobile_no=454565456,  last_name='tendulkar'))


# def sum():
#     a = 2 + 3
#     return a
#
# print(sum())


def all_squared_numbers(start, end):
    square_no = []
    print('Starts with:', start, 'Ends with :', end)
    for k in range(start, end+1):
        square_no.append(k*k)

    return square_no


print(all_squared_numbers(start=5, end=10))


def sum(a, b):
    print("Sum of:", a, b)
    return a + b


def sub(a, b):
    return a -b


def mul(a, b):
    return a * b


def div(a, b):
    return a/b

s = sum(a=56456456, b=5666,)

print(s)

print(sub(a=70, b=5))

def sum_all(*args):
    print('My args :---', args)
    s = 0
    for i in args:
        s = s+i
    return s

print(sum_all(4,56,6,6,8,9, 45645646,58789789789,7897,897,897,87,897,87,89))


def mull_all(*args):
    print('My args', args)

    m = 1
    for i in args:
        m = m*i
    return m

print(mull_all(1,2,3,564,4545,454))


def conact_names(**kwargs):

    print('My kwargs', kwargs)
    s = ''
    for i in kwargs:
        print(kwargs[i])
        s = s + kwargs[i]

    return s

print(conact_names(name='sree', last_name='kaluri'))