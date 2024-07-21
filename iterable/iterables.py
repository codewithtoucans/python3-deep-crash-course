# How to copy a sequence
# shallow copy or deep copy
# from copy import copy, deepcopy

# The slice type
s = slice(0, 2)
l = [1, 2, 3, 4, 5]
print(l[s])

# range
print(range(8))


# custom sequence
# a minimum implement methods: __len__ and __getitem__
class Fib:
    from functools import lru_cache

    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                index = self.n + index
            if index < 0 or index >= self.n:
                raise IndexError
            return Fib._fib(index)
        if isinstance(index, slice):
            start, stop, step = index.indices(self.n)
            return [Fib._fib(i) for i in range(start, stop, step)]

    @staticmethod
    @lru_cache(maxsize=20)
    def _fib(n):
        if n < 2:
            return 1
        return Fib._fib(n - 1) + Fib._fib(n - 2)


f = Fib(10)
print(f[9])
print(f[-1])
print(f[0:5])
print(f[0:5:2])

# In-place concatenation and repetition
# if object is mutable, it is in-place += and *=
# if object is immutable, it is not in-place += and *=
# list concatenation
a = [1, 2, 3]
print(id(a))
b = [4, 5, 6]
a += b
print(id(a))

# concatenation and in-place concatenation
# overloaded these operators by methods: __add__ __iadd__

# repetition and in-place repetition
# overloaded these operators by methods: __mul__ __imul__

# slicing accessing elements
# overloaded these operators by methods: __getitem__

# assignment
# overloaded these operators by methods: __setitem__

# additional sequence functions and operators
# __contains__ __delitem__ __rmul__ __radd__

# sort sequence
# overloaded these operators by methods: __lt__
# use sorted method to sort sequence, it is not in-place
c = sorted(b, reverse=True)
# use sort method to sort sequence, it is in-place
b.sort()

# list comprehensions
# [expression for x in iterable if condition]
d = [x * 2 for x in range(10)]
print(d)

# The iterator protocol
# __iter__ return itself
# __next__ return next element
# an object that implements these two methods is called an iterator


# The iterable protocal
# __iter__ return a new instance of the iterator object
# an object that implements these two methods is called an iterable
class Cities:
    def __init__(self):
        self.cities = ["Shanghai", "Beijing", "Guangzhou", "NanJing"]

    def __len__(self):
        return len(self.cities)

    def __iter__(self):
        return self.CityIterator(self.cities)

    class CityIterator:
        def __init__(self, cities):
            self.cities = cities
            self.current = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.current >= len(self.cities):
                raise StopIteration
            city = self.cities[self.current]
            self.current += 1
            return city


c = Cities()
print(list(c))
print(sorted(list(c), reverse=True))

# iter() function will call the __iter__ method which implements the iterator protocol
# will call the __getitem__ method which implements the sequence protocol

# reversed() function will call the __reversed__ method which implements the iterator protocol


# Generators
# A function that uses the yield statement, is called a generator function
# Generators are iterators, Generators implements the iterator protocol
def fib(n):
    for i in range(n):
        yield Fib._fib(i)


fb = fib(8)
print(list(fb))

# Generator expression
g = (Fib._fib(i) for i in range(5))
print(list(g))


# yield from
def read_file():
    with open(".gitignore", "r", encoding="utf-8", errors="ignore") as f:
        yield from f


file = read_file()
print(file)

# itertools.islice return a lazy iterator
# itertools.filterfalse retains elements where the predicate evaluates to False
# itertools.compress a way of filtering one iterable, using the truthiness of items in another iterable
# itertools.takewhile retains elements from an iterable while the first element is true
# itertools.dropwhile retains elements from an iterable while the first element is false

# itertools.count return a lazy iterator that generates an infinite sequence of numbers
# itertools.cycle return a lazy iterator that repeats an iterable indefinitely
# itertools.repeat return a lazy iterator that repeats an object indefinitely or finite

# itertools.chain return a lazy iterator that chains multiple iterables together
# itertools.tee return a generator of multiple iterators

# itertools.starmap
# itertools.accumulate
# itertools.zip
# itertools.zip_longest
# itertools.groupby
# itertools.product
# itertools.permutations
# itertools.combinations
