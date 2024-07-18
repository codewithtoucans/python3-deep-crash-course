# Scopes and Namespaces

# Global scopes are nested inside the built-in scope

# The global keyword


a = 0


def my_func():
    # global a
    a = 100
    print(a)


my_func()
print(a)


# The nonloacl keyword
def outer_func():
    x = "hello"

    def inner_fun():
        # nonlocal x
        x = "world"
        y = 100
        print(y)

    inner_fun()
    print(x)


outer_func()


# Closures
# You can think of the closure as a function plus an extended scope that contains the free variables


# The label x is in two different scopes but always reference the same 'value'
# python does this by creating a cell as an intermediary object
# in effect, both variables x (in outer and inner), point to the same cell
# when requesting the value of the variable, python will 'double-hop' to get to the final value
def outer():
    x = "python"

    def inner():
        print(x)

    return inner


fn = outer()
# introspection
print(fn.__code__.co_freevars)
print(fn.__closure__)


def adder(n):
    def inner(x):
        return x + n

    return inner


a = adder(10)
b = adder(20)

print(a(5))
print(b(5))
print(a.__closure__)
print(b.__closure__)

# this is a error example
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[0].__code__.co_freevars)
print(adders[1].__code__.co_freevars)
print(adders[2].__code__.co_freevars)


# closure applications
# simplify a class with a method that needs to access the class instance
class Averager:
    def __init__(self) -> None:
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)


a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))


def average() -> callable:
    numbers = []

    def inner(number: int) -> float:
        numbers.append(number)
        return sum(numbers) / len(numbers)

    return inner


ave = average()
print(ave(10))
print(ave(20))
print(ave(30))


# closures and decorators
def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def counter(fn, c):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        c[fn.__name__] = count
        return fn(*args, **kwargs)

    return inner


c = {}
add = counter(add, c)
mult = counter(mult, c)
print(add(10, 20))
print(mult(10, 20))
print(add(10, 20))
print(mult(10, 20))
print(c)
