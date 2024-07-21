# namedtuple
# the subclass tuple, and add a layer to assign property names to the positional elements
# the namedtuple has a keyword-only argument, rename (default false)
# that will automatically rename any invalid field name
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Point = namedtuple("Point", ("x", "y"))
Point = namedtuple("Point", "x y")
Point = namedtuple("Point", "x, y")
p = Point(1, 2)
print(p.x, p.y)

# Introspection
print(Point._fields)
print(Point._asdict(p))

# Unpacking namedtuple
x, y = p
print(x, y)

# The _replace instance method to modify a namedtuple
# Due to the tuple subclass, the original object is not modified
# p.x = 10 -> read only
p = p._replace(x=10)
print(p)

# Extending a namedtuple
Point3d = namedtuple("Point3d", Point._fields + ("z",))
p3d = Point3d(1, 2, 3)
print(p3d)

# Using namedtuple to return multiple values
Color = namedtuple("Color", "red green blue alpha")


def random_color():
    import random

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return Color(r, g, b, 255)


# this will have IDE tips
color = random_color()
print(color)
print(color.blue)

# translate dict to namedtuple or namedtuple to dict
print(color._asdict())

c = {"red": 1, "blue": 2, "green": 3, "alpha": 4}
Cl = namedtuple("Cl", c.keys())
cl = Cl(**c)
print(cl)
