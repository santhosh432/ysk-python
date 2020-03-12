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