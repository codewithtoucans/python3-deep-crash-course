# positional arguments
# via the order in which they are passed

# default values
# a positional arguments can be made optional by specifying a default value for the corresponding parameter

# keyword arguments
# via the name of the argument
# all arguments after the first named (keyword) argument, must be named too
# default arguments may still be omitted

# packed values
# any iterable can be considered a packed value

# unpacking packed values
# unpacking is the act of splitting packed values into individual values
# unpacking works with any iterable type
a, b, c = [1, 2, 3]
a, b, c = "ABC"

# use unpacking to swap values
a, b = b, a

# extending unpacking
# use * to unpack, can only be used once in LHS
a, *d = [1, 2, 3, 4, 5]
a, *d = "helloworld"
a, *d, c = "helloworld"
*d, c = "helloworld"

# use ** to unpack key-value paris of the dictionary
e = {"a": 1, "b": 2, "c": 3}
f = {"a": 10, "d": 4}
g = {**e, **f}
print(g)
g = {**f, **e}
print(g)

# unpacking nested values
a, *b, (c, *d) = [1, 2, [3, 4]]
print(a, b, c, d)

# *args argument
# *args is a tuple
# *args exhausts positional arguments


# keyword arguments
# function parameters after *, must be keyword arguments
def hello(*, d):
    pass


# **kwargs argument
# **kwargs is a dictionary
# **kwargs exhausts keyword arguments


# In general, always beware of using a mutable object (or a callable) as a argument default value
from datetime import datetime


def log(msg, *, dt=datetime.now()):
    print("{0} {1}".format(dt, msg))
    pass


log("hello")
log("world")
log("push")


def add_item(itme, item_list=[]):
    item_list.append(itme)
    return item_list


item1 = add_item(1)
add_item(2)
item2 = add_item(3)
print(item1)
print(item2)
