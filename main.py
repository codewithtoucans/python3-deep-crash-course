# Docstrings
# stored in the function's __doc__ property
# use help() function
def hello(a, b, /):
    """say hello"""
    print("hello")


print(hello.__doc__)


# function annotations
# stored in the __annotations__ property of the function
# type hinting
def world(a: int) -> None:
    """world function"""
    print(a)


print(world.__annotations__)

# Lambda Expressions
# lambda expressions are anonymous functions
# lambda expressions are used to create short, one-line functions
# lambda [parameters] : expression, the expression return a function object

# the function body of lambda is limited to a single expression
# no assignments
# no annotations or type hinting
# single logical line of code
square = lambda x: x**2
print(type(square))
print(square(5))


# functions introspection
# functions are first-class objects, they have attributes, we can attach our own attributes
# functions can be assigned to variables
# functions can be passed as arguments
# functions can be returned from other functions
# functions can be stored in data structures
hello.category = "world"
print(hello.category)

# the dir() function returns a list of the attributes of an object
# __name__ name of function
# __defaults__ tuple containing positional parameter defaults
# __kwdefaults__ dictionary containing keyword parameter defaults
# __code__ the code object associated with the function, has various properties,
# like co_varnames, co_argcount(not containing *args and **kwargs), etc.
print(dir(hello))
print(hello.__defaults__)
print(hello.__kwdefaults__)
print(hello.__code__.co_varnames)
print(hello.__code__.co_argcount)


# The inspect module
import inspect

print(inspect.getsource(hello))
print(inspect.getmodule(hello))
print(inspect.getcomments(hello))
print(inspect.signature(hello))

for param in inspect.signature(hello).parameters.values():
    print(param.name, param.default, param.annotation, param.kind)


# callables
# objects that can be called will return True
print(callable(print))

# High Order Functions
# functions that take other functions as arguments
# functions that return other functions
# functions that return functions
# eg: map sorted filter reduce zip

# partial function to reduce the parameters

# built-in reducing functions
# eg: min max sum any all

# the operator module
