
"""
    Topic: Data Structure's
    Author: YSK-PYTHON
    python : 3.5.2

"""

# 1.Create a list with random numbers and find length of list?
# 2.Create a list with some number sand check an item exists in the list or not?
# 3.Remove the last and first item in the list.
# 4.Write a programme finding a duplicate elements in the list.
# 5.Write a programme to get a unique numbers in a list .

# 1. scores = {'palyer1': [23,56,8,98,100], 'player2': [89,25,6,3,6], 'player3': [0,2,5,6,9]} ,
#  form the given dictionary find the total score of eac player , the output will in the given format
# total_scores = {'player1' : 25, 'player2': 2, 'player3': 25}

# 2. Find the average of all players in the above scores dictionary object.

# 3 my_list = [100, 200, 100, 200,300,100,100,200]
# write a programe to number of times repeated in the list.
# {100 : 3, 200:3, 300:1}

# 4.Write a programme to display in the given format .

# *
# * *
# * * *
# * * * *
# * * * * *

# 5. my_numbers = [8,9,6,56,94,3,6,5,63,1,2,5,87,8,33,45,7,775,4845,85,96,4]
# create a new list with numbers which all are divisible by both 3 and 5 .
# create a new list with numbers which all are divisible by either 5 or 7.



scores = {'palyer1': [23,56,8,98,100], 'player2': [89,25,6,3,6], 'player3': [0,2,5,6,9]}

total_scores = {}
print('Before ', total_scores)


for keys, values in scores.items():
    print(keys, '-----',  values)
    total_scores[keys] = sum(values)

print('After', total_scores)


avg_scores = {}

for k, v in scores.items():
    print(k , v)
    avg_scores[k] = round(sum(v)/len(v))

print(avg_scores)


max_scores ={}

for k , v in scores.items():
    print(k, v)
    max_scores[k] = max(v)

print('Max scores', max_scores)





# 3.

my_list = [100, 200, 100, 200,300,100,100,200]

repeat_number = {}

for i in my_list:
    if i in repeat_number:
        repeat_number[i] = repeat_number[i] + 1

    else:
        repeat_number[i] = 1
    print(repeat_number)

print('repeat_number',repeat_number)


h = {}

for k in my_list:
    h[k] = h.get(k, 0) + 1

print(h)




print('=' * 100)
my_list = [100, 200, 100, 200,300,100,100,200]
print(my_list)

print(set(my_list))
u_values = set(my_list)
h = {}

for i in u_values:
    print(i,'======', my_list.count(i))
    h[i] = my_list.count(i)

print(h)



runs = 1 # 0.5, 0.25, 0.125
for k in range(6):
    # print(k)
    runs = runs / 2  # 0 + 1
    print(k, runs)

print(runs)







