# Decorators

# takes a function as an argument
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


# Decorators Application (Timer)
def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*arg, **kwargs):
        start = perf_counter()
        result = fn(*arg, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in arg]
        kwargs_ = ["{}={}".format(k, v) for k, v in kwargs.items()]
        all_args = args_ + kwargs_

        name = fn.__name__
        args_str = ", ".join(all_args)
        print(f"{name}({args_str}) took {elapsed:.6f} seconds")

        return result

    return inner


@timed
def calc_recurseive_fib(nums):
    if nums < 2:
        return nums
    return calc_recurseive_fib(nums - 1) + calc_recurseive_fib(nums - 2)


# calc_recurseive_fib(4)


# Stacked Decorators
# There is some different in python3.9
def dec_1(fn):
    def inner():
        print("decorator 1")
        return fn()

    return inner


def dec_2(fn):
    def inner():
        print("decorator 2")
        return fn()

    return inner


def dec_3(fn):
    def inner():
        print("decorator 3")
        return fn()

    return inner


@dec_1
@dec_2
@dec_3
def h():
    print("h")


h()


# Decorators with Parameters
# You can think this is a function that return a decorator
def outer(num):
    def timed(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*arg, **kwargs):
            elapsed = 0
            for i in range(num):
                start = perf_counter()
                result = fn(*arg, **kwargs)
                end = perf_counter()
                elapsed += end - start

            elapsed /= num

            args_ = [str(a) for a in arg]
            kwargs_ = ["{}={}".format(k, v) for k, v in kwargs.items()]
            all_args = args_ + kwargs_

            name = fn.__name__
            args_str = ", ".join(all_args)
            print(f"{name}({args_str}) took {elapsed:.6f} seconds")

            return result

        return inner

    return timed


@outer(5)
def hello():
    print("Hello world")


hello()


# Class Decorator
class Myclass1:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *arg, **kwargs):
        print("class decorator")
        return self.fn(*arg, **kwargs)


@Myclass1
def world(a, b, c):
    print(f"world a={a}, b={b}, c={c}")


world(1, 2, 3)


# Class Decorators with Parameters
class Myclass2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("class decorator with parameters ", self.a, self.b)
            return fn(*args, **kwargs)

        return inner


@Myclass2(10, 20)
def world1():
    print("world1")


world1()
