"""Lists methods:
    remove(item)
    append(item)
    sort()
    pop(index)
"""

# my_list = [1, 2, 3]
# my_list.append(0)
# print(my_list) 

# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)

# my_list = [3, 1, 4, 2]
# my_list.sort()
# print(my_list)

# my_list = [1, 2, 3, 4]
# item = my_list.pop(1)
# print(item) 
# print(my_list)


"""Dictionary Methods:
    keys()
    values()
    items()
    get(key)
"""

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.keys()) 


# dictionary = {'a': 1, 'b': 2, 'c': 3}
# # print(dictionary.values())
# dictionary["a"] = 90
# print(dictionary.values())

# my_dict = {'a': 10, 'b': 25, 'c': 31}
# print(my_dict.items())

# my_dict = {'a': 12, 'b': 45, 'c': 8}
# print(my_dict.get('b'))


"""Set Methods:
    add(item): Add item to the set
    remove(item): Remove item from the set
    union(set): Return union of sets
    intersection(set): Return a new set that contains only the elements that are present in both sets
"""
# my_set = {1, 2, 3}
# my_set.add(2)
# print(my_set)

# my_set = {1, 2, 3, 4}
# my_set.remove(4)
# print(my_set)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set2.union(set1)
# print(union_set)

# set1 = {1, 3, 7}
# set2 = {4, 5, 4}
# intersection_set = set2.intersection(set1)
# print(intersection_set)

"""Tuple methods:
    count(item): Return the number of occurrences of item in a tuple
    index(item): Return the first index of item in a tuple

"""
# my_tuple = (1, 3, 4, 2)
# count = my_tuple.count(2)
# print(count)

# my_tuple = (1, 3, 2, 3, 2, 4, 2, 3)
# index = my_tuple.index(3)
# print(index) 