#
# """
#     Topic: Data Structure's
#     Author: YSK-PYTHON
#     python : 3.5.2
#
# """
#
#
# # what is data structure?
#
# # The efficient way to store a data .
#
# # List
#
# list_one = []
#
# print(list_one)
#
# list_one.append(50)
# list_one.append(3)
# list_one.append(100)
# print(list_one)
#
# print('==========================')
#
#
# list_one.extend([30,105])
#
# print(list_one)
#
#
# list_one.insert(0, 10)
#
# list_one.insert(3, 6)
#
# print(list_one)
#
#
# list_one.remove(10)
#
# print(list_one)
#
# list_one.pop()
#
# print(list_one)
#
#
# list_one.pop(0)
# print(list_one)
#
# print(list_one.count(3))
#
#
# # generating list
#
#

list_two = []
print("Before :", list_two)
for i in range(1, 11):
    list_two.append(i*i*i)

print('After', list_two)

print(list_two[0:5])

print(list_two[6:9])
print(list_two[-6:-1])


l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2

print(l3)

l3[0] = 6

print(l3)

l3[3] = 100

print(l3)

# tuple

tup = (50,60,80,100)


print(tup)


print(type(list_two))

print(type(tup))

print("=============== SET ================")
# ============= Set ================

s1 = set()
print(s1)

s2 = {100,20,52,12,23,98, 98, 100}
print(s2)

print(type(s2))


print('=============== DICT ================')

d1 = {}
print(d1)

d2 = {'name': 'sreeram', 'place':'hyderabad'}
print(d2)

d2['height'] = 6

d2['weight'] = 50
print(d2)

d3 = {}

for i in range(1, 101):
    d3[i] = i*i*i

print(d3)

# print(d3[200])


print(d3.get(200, 'This is not exists'))

student_marks = {'101': 20, '102':30, '103':45}

print(student_marks)

# print(student_marks['105'])

print(student_marks.get('103', 'Absent'))

regno = '102'

if regno in d3:
    # print(regno, 'Exist')
    print(d3[regno])
else:
    # print(regno, 'Not exist')
    print('Absent')



## list comprehensions


print('================ LIST COMP ========================')
cubes_of_elements = [i*i*i for i in range(1, 11)]

print(cubes_of_elements)


even_numbers = tuple(i for i in range(1,101) if i % 2 == 0)

# even_numbers = []
# for i in range(1, 101):
#     print('My items', i)
#
#     if i%2 == 0:
#         print('check', i)
#         even_numbers.append(i)

print(even_numbers)

print(type(even_numbers))

#####  dict comp =======

d_comp = {i:i*i*i for i in range(1,101) if i %5 == 0}

print(d_comp)

