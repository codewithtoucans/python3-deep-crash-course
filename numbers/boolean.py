# booleans are subclass of int
print(issubclass(bool, int))
print(int(True))
print(int(False))

# bool(0) -> False
# bool(x) -> True for any int x != 0

# every object has a ture value except:
# None
# False
# 0 in numeric type
# empty sequences or mapping types
# custom classes that implement a __bool__ or __len__ reutrn 0 or false
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))

# the boolean operators: not, and, or

# short-circuit evaluation
# x or y will return true without evaluating y if x is true
# x and y will return true without evaluating y if x is false

# x and y / x or y will not return a bool value
# x or y -> if x is true, return x, otherwise evaluates y return it
# x and y -> if x is false, return x, otherwise evaluates y return it
print(0 or 19)
print(12 or 19)
print(0 and 19)
print(12 and 19)

# comparision operators
# is / is not
# in / not in
# > < >= <= == !=
