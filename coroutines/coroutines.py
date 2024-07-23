# implement a producer/consumer using subroutines
from collections import deque


def produce_elements(dq: deque):
    for i in range(100):
        dq.appendleft(i)


def consume_elements(dq: deque):
    while len(dq) > 0:
        print(f"processing item, {dq.pop()}")


def coordinator():
    dq = deque()
    produce_elements(dq)
    consume_elements(dq)


coordinator()


# implement a producer/consumer using coroutines
def produce_elements_co(dq: deque, n: int):
    for i in range(n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            # yield control
            yield


def consume_elements_co(dq: deque):
    while True:
        while len(dq) > 0:
            print(f"processing item, {dq.pop()}")
        # yield control
        yield


def coordinator_co(n: int):
    dq = deque(maxlen=10)
    producer = produce_elements_co(dq, n)
    consumer = consume_elements_co(dq)
    while True:
        try:
            next(producer)
        except Exception:
            break
        finally:
            next(consumer)


coordinator_co(100)

# Generator States
# from inspect import getgeneratorstate
# four state:
#    1. GEN_CREATED
#    2. GEN_RUNNING
#    3. GEN_SUSPENDED
#    4. GEN_CLOSED
# print(getgeneratorstate(gen))


# Send data to generator only when generator state is GEN_SUSPENDED
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


a = average()
next(a)
print(a.send(10))
print(a.send(20))
print(a.send(30))


def average_closure():
    total = 0.0
    count = 0

    def inner(value):
        nonlocal total
        nonlocal count
        total += value
        count += 1
        return total / count

    return inner


avg = average_closure()
print(avg(10))
print(avg(20))
print(avg(30))

# close generator
# when generator .close() is called, a GeneratorExit exception is triggered inside the generator
# it's perfectly OK not to catch it, and simply let it bubble up
# when generator .throw(exception) is called, throwing an exception to the coroutine
# the exception is raised at the point where the coroutine is suspended


# use decorators to make coroutine
def coroutine(fn):
    def prime(*args, **kwargs):
        gen = fn(*args, **kwargs)
        next(gen)
        return gen

    return prime


@coroutine
def average_coroutine():
    total = 0.0
    count = 0
    average = None
    while True:
        try:
            term = yield average
            total += term
            count += 1
            average = total / count
        except TypeError:
            print("type error")


print("-" * 30)
c = average_coroutine()
print(c.send(10))
print(c.send(20))
print(c.send(30))
print(c.send(40))
print(c.throw(TypeError("abc")))
print(c.close())
