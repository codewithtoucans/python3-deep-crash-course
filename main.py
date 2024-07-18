# Decorators

# takes a fucntion as an argument
# returns a closure
# the closure usually accepts any combination of parameters
# runs some code in the inner function (closure)
# the closure function calls the original function using the arguments passed to the closure
# returns whatever is returned by that function call
from typing import Any


def counter(fn: callable) -> callable:
    count = 0

    def inner(*arg: Any, **kwargs: Any):
        nonlocal count
        count += 1
        print(f"{fn.__name__} has been called {count} times")
        return fn(*arg, **kwargs)

    return inner


def add(a: int, b=1) -> int:
    return a + b


add = counter(add)
print(add(10, 20))
print(add(5))


# Decorators and the @ symbol
@counter
def mult(a: int, b: int) -> int:
    return a * b


print(mult(10, 20))
print(mult(12, 2))

# Introspecting Decorated Functions
print(f"add function name: {add.__name__}")
# print(help(add))


print(f"mult function name: {mult.__name__}")
# print(help(mult))
# Using functools module to fix the metadata of our inner function in our decorator
import functools


def new_counter(fn: callable) -> callable:
    count = 0

    @functools.wraps(fn)
    def inner(*arg: Any, **kwargs: Any):
        nonlocal count
        count += 1
        print(f"{fn.__name__} has been called {count} times")
        return fn(*arg, **kwargs)

    return inner


def div(a, b):
    return a / b


div = new_counter(div)
print(div(10, 20))
print(f"div function name: {div.__name__}")
# print(help(div))
