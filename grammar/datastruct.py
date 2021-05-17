# The 4 built-in data types used to store collections of data


# list
"""
lists can be used to dinamically manipulate sequences
as they are mutable. for this reason they cause more
overhead than tuples since memory is allocated more
often.
"""
l1 = [1, 2, 3, 4, 5]
l2 = list((1, 2, 3, 4, 5))

# tuple
"""
tuples represent static sequences of objects. as such
it is not possible to shallow copy a tuple (unlike lists).
"""
t1 = (1, 2, 3, 4, 5)
t2 = tuple([1, 2, 3, 4, 5])

# dictionary
"""
dictionaries stores data in key: value pairs. they are
mutable, ordered (after 3.7) and do not allow duplicate keys.
under the hood an hash table is used to map keys to values.
"""
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict(a=1, b=2, c=3)

# set
"""
sets are unordered, unchangable, unindexed, collection
of unique items. They allow for set operations like
subsetting, union, intersection...etc
"""
s1 = {1, 1, 2, 2, 3, 3}
s2 = set((1, 1, 2, 2, 3, 3))
