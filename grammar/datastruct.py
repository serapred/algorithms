# The 4 built-in collection-oriented data types

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
they are immutable and it is not possible
to perform shallow copies  (unlike lists).
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
s1 = {1, 1, 2, 2, 3, 3}         # set(1,2,3)
s2 = set((1, 1, 2, 2, 3, 3))    # same


# notes
"""
On variables passing:
    Variables in python are passed by object-reference.
    it is an hybrid approach (between passing references or values)
    since it pass a reference to the object in memory to the function
    (side note, everything in python is 1st class object)
    but the function create a copy of such reference.
    This means  you can interact with the object in memory
    within the function, without affecting the caller reference reference.
"""
