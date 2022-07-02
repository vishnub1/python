# Set is a unorder collection of Unique element

# - the set in pyhon are typically usd for mathematically used mathematical
#   operations like union,intersection,difference and complement etc.

#  we can create a set,access its element and carry out these mathematical operations.
#  {1,2,3,344,}

a={1,9,5,3,4,5,};
print(type(a));     # <class 'set'>

print(a);           # {1, 3, 4, 5, 9}      unorder collection of unique element

# updating set
a.add(6);
print(a);           # {1, 3, 4, 5, 6, 9}

# Deleting the set
b={'a','b','c'}
print(b);           # {'b', 'a', 'c'}

"""
>>> b={'x','a','v'};
>>> print(b);
{'v', 'a', 'x'}
>>> b.discard('a');
>>> print(b);
{'v', 'x'}
>>>
"""
