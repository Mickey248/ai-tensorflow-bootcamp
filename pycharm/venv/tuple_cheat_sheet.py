"""
-By convention, we generally use tuple for different datatype and list for similar datatypes
-Since tuple are immutable, then iterating through tuple is faster than with list!!!
-Tuples that contain immutable element can be used as key for a dictionary. With list, this is NOT possible.
-if you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected
"""

#Empty tuple
tuple1 = ()
print(tuple1)

tuple1 = (1 ,2 ,3)
print(tuple1)

tuple1 = (1, 'hello', 3.4)
print(tuple1)

#nested tuple
tuple1 = ('mouse', [8, 4, 6], [1, 2, 3])
print(tuple1)

# How to check 'type' in python
print(type(tuple1))

# creating a tuple is not necessary to use '()'
tuple2 = 1,2,3
print(type(tuple2))

tuple3 = (1,)
print(type(tuple3))

tuple4 = 1,
print(type(tuple4))
