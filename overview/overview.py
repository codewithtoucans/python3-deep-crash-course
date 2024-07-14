"""
Identifier names
case-sensitive

rules:
start with _ or letter, followed by any _ or letters or digits
cannot be reserved words

Conventions:
_my_var     This is a convention to indicate 'internal use' or 'private' objects
__my_var    Used to 'mangle' class attributes - useful in inheritance chains
__my_var__  Used for system-defined names that have a special meaning to the interpreter

PEP 8 Style Guide:
https://www.python.org/dev/peps/pep-0008/

Packages    short, all-lowercase names. Preferably no underscores.
Modules     short, all-lowercase names. Preferably have underscores.
Classes     Capitalized names. Upper Camel Case.
Fkunctions   Snake case.
Variables   Snake case.
Constants   All uppercase. words separated by underscores.

"""

# Variables in python are always references and refer to objects in memory
# we can find out the mmemory address of an object by using the id() function
my_var = 10
print(my_var)
print(id(my_var))
print(hex(id(my_var)))

# Reference count
# sys.getrefcount()
# ctypes.c_long.from_address().value

# built-in type() function to determine the type of the object currently referenced by a variable
print(type(my_var))
my_var = "Hello World"
print(type(my_var))

# an object whose internal state can be changed, is called mutable
# Lists are mutable
# Sets are mutable
# Dictionaries are mutable
# User Defined Classes are mutable

# an object whose internal state cannot be changed, is called immutable
# Numbers are immutable
# Strings are immutable
# Tuples are immutable
# Frozen Sets are immutable
# User Defined Classes are immutable

# With mutable objects, the python memory manager will never create shared references.
# With immutable objects, the python memory manager will create shared references.

# Variable equality in two fundamental ways
# Memory Address identity operator is  is not
# Object State(data) equality operator == !=

# Everything in python is objects

# force strings to be interned by using the sys.intern() function

# Set membership is much faster than list or tuple membership

# the Zen of python
# import this
