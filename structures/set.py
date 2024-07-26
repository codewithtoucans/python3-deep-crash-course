# set is an unordered collection of distinct objects

# create set
# {} this is an empty dict
s = {1, 2, 3}
print(s)
s = set()
print(s)
s = set([1, 2, 3])
print(s)

# membership
# in / not in
print(1 in s)

# unpacking set
print(*s)

# set operations
# union |
# intersection &
# difference -
# symmetric difference ^
# isdisjoint
# issubset <=
# issuperset >=
f = {1, 2, 3, 4}
s = {3, 4, 5, 6}
print(f | s)
print(f & s)
print(f - s)
print(f ^ s)
print(f <= s)
print(f >= s)

# analogous set mutating updates
# |=
# &=
# -=
# ^=
# update
# intersection_update
# difference_update
# symmetric_difference_update

# copy & deepcopy

# frozenset
# frozenset is an immutable version of set, can hashable
s = frozenset(s)
print(s)
