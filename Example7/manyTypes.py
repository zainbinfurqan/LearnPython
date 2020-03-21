
# -----------------list -----------------
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list
list_alphabates = ['a', 'b', 'c', 'd']

# print(list_alphabates[0]) # it will print the element from zero index

list_a.append(100)  # add element to end of the list
list_a.pop(5)  # remove element from index which is provided
list_a.reverse()  # reverse the list elements
# insert elemebt at given index (index num, element to isert)
list_a.insert(2, 1)

# return the count of number present in list which is given in ()
# print(list_a.count(4))

# print(list_a)

# print(list_a.index(1))

# list_a.sort()
# print(list_a)

# ------------disionary------------------

disionary_1 = {"name": 'Zain', "age": 23, "designation": 'software developer'}
disionary_1['name'] = "omer"

disionary_2 = [
    {"name": 'omer', "age": 23},
    {"name": 'tanveer', "age": 23},
    {"name": 'ammad', "age": 23},
    {"name": 'arshaq', "age": 23}
]

# print(disionary_1['name'])
# print(disionary_1)

print(disionary_2)

# print  disionary data with for loop
for data in disionary_2:
    print(data.get('name'), data['age'])

#------------symmetric_difference ----------#

data_1 = {'a', 'b', 'c', 'e', 'g', 'j', 'm'}
data_2 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# will only work on that kind of data and structure type
result = data_1.symmetric_difference(data_2)

print(result)
