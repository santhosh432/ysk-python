
# map


#map(function, iterable)


my_list = [2,3,4,5,6]

my_names = ['sachin', 'sreeram', 'santhosh']

def cube(x):
    return x ** 3


def length(x):
    return len(x)


# print(list(map(len, my_names)))
# ===============================================
# filter


# filter(function , iterable)

my_numbers = [2,5,87,9,3,4,5,25,5,4]

def even(x):
    return x %2 == 0 # true or false

print(list(filter(even, my_numbers)))


print(list(filter(lambda x : False if x % 2 ==0 else True, my_numbers)))




my_scores = [105,10,6,20,6,85,3,6,4,5,78,9,225,6111,222,33]

def century(x):
    return x >= 100

print(list(filter(century, my_scores)))


# reduce


# reduce(function , iterbale)

my_num = [2,8,9,34,11,2,36]

def min_number(x, y):
    if x > y:
        return y
    else:
        return x

def max_number(x, y):
    if x > y:
        return x
    else:
        return y

from functools import reduce

# print(reduce(min_number, my_num))

print(reduce(max_number, my_num))

