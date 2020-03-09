"""
    Topic: Numbers & Strings
    Author: YSK-PYTHON
    python : 3.5.2

"""


# If and else Statements

"""
syntax :

if condition:
    # do something
else:enumerate
    # do something

"""


score = 105

if score >= 100:
    print('Century')

else:
    print('Not a century')


# if, elif and else

age = 26

if 0 < age <= 10:
    print('Small')
elif 10 < age <= 20:
    print('Medium')
else:
    print('Large')

# if , else with multiple conditions
age = 19
height = 4

if age <= 19 and height >= 4:
    print('Eligible for under 19 cricket team')
else:
    print('Eligible')


# For loop statements

for i in 'I am a developer':
    print(i)

i = 0
for k in 'hello':
    print('Index', i, 'value', k)
    i += 1  # i = i +1

# while Statement

a = 0

while a < 6: # also a <= 5
    print(a)
    a += 1  # increment by 1

# range function

# need to iterate over sequence of numbers


for i in range(5, 10):  # range(start , end))
    if i == 7:
        print('Accept', i)
    else:
        print('Not accept', i)


# eg: range(start, end, gap)


# control statements

# break
for i in range(1, 10):

    if i%3 == 0:
        break
    print('I is ', i)

print('The end')

print('==============')

# continue

for j in range(1, 20):
    if j % 3 == 0:
        continue
    print('J is ', j)


# enumerate

# iterate over sequence of items along with index positions

for i, j in enumerate('seetharam'):
    print('Index position', i, 'Real value', j)



