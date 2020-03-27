# exercise

# 1 . Write a python programme to find out sum of each list objects in the given list.

my_marks = [[60,78,56,96,45], [45,69,85,67,49], [54,89,63,75]]

# 2. Write a python prgrame to get fullname of each dict object

my_name = [{'first_name': 'sachin', 'last_name': 'Tendulkar'},
           {'first_name': 'virat', 'last_name':'kohli'},
           {'first_name':'MS', 'last_name':'Dhoni'}]

# 3. Write a python programme to get a list of list items which contains at least one century in the give list

my_scores = [[25,100,20,30], [56,89,65,12], [54,105,103]]

# 4. Find the sum and multiplication of all elements in the given tuple.

my_items =(2,3,6,9,6,7)


# sol

def full_name(name):
    print(name['first_name'])
    print(name['last_name'])
    fullname = {'full_name': name['first_name'] + name['last_name']}
    return fullname

print(full_name({'first_name': 'sachin', 'last_name': 'Tendulkar'}))


print(list(map(full_name, my_name)))


print(list(map(lambda x: {'full_name': x['first_name'] + x['last_name']}, my_name)))