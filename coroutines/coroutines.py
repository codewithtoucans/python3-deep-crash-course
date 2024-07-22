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
