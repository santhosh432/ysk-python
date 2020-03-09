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
else:
    # do something

"""

# Answer below questions in python.

# 1. Declare a variable batsmen_score check that half century ot not ?

# 2. Check a batsman score for century or double century or triple century?

# 3. Writ a python programme to Check leap year?

# 4. Write a Python Program to Check Prime Number?

# 5. Write a Python programme 1 to 10 th table (from 1 to 10).



score = 105

if score >= 100:
    print('Century')
else:
    print('Not a century')


# if, elif and else

age = 15

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

for k in 'hello':
    print(k)


# while Statement

a = 0

while a < 5:
    print(a)
    a += 1  # increment by 1

# range function

# need to iterate over sequence of numbers


for i in range(10):
    print('Number:', i)


# eg: range(start, end, gap)


# control statements

# break
for i in range(1, 10):
    if i%5 == 0:
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



