# dict
# the key must be hashable, if two objects compare equal(==), the hashed must be equal
# two objects that do not compare equal, may still have the same hash (hash collision)
# python3.6+, in addition, the order is same as dictionary insertion order

# create dict
d = {}
print(d)
d = {"one": 1, "two": 2, "three": 3}
print(d)
d = dict()
print(d)
d = dict.fromkeys([1, 2], 3)
print(d)

# create key if it does not exist
# assign value if it exists
d[3] = 1
d[3] = 10
print(d)

# return the value for specified key, if key not exists raise KeyError exception
# print(d[10])


# return the value for specified key, if key not exists return default value
print(d.get(10, "default"))

# membership
print(3 in d)
print(10 not in d)

# setdefault method

# dict views
print(d.keys())
print(d.values())
print(d.items())

# dict views operations
e = {"one": 1, "two": 2, "three": 3}
# union
print(d.keys() | e.keys())
# intersection
print(d.keys() & e.keys())
# difference
print(d.keys() - e.keys())

# update method
# later key-value will overwrite/insert previous key-value
f = {4: 4, 3: 50}
d.update(f)
print(d)


# unpacking dictionaries
d = {**d, **e}
print(d)


# dictionary copy
# shallow copy
d_copy = d.copy()
d_copy = {**d}
d_copy = dict(d)
d_copy = {k: v for k, v in d.items()}

# deep copy
# d_copy = copy.deepcopy(d)


# manually hash
class Person:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)


p1 = Person("John")
p2 = Person("Tom")
h = {p1: "John", p2: "Tom"}
print(h)
print(h[p1])
