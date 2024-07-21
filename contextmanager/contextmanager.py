# The context management protocol
# implements the context manager protocol: __enter__ __exit__
# Not just a context manager
from io import TextIOWrapper


class DataIterator:
    def __init__(self, fname) -> None:
        self._fname = fname
        self._f: TextIOWrapper

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self._f)
        return row.strip("\n").split(",")

    def __enter__(self):
        self._f = open(self._fname)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False


with DataIterator(".gitignore") as f:
    for row in f:
        print(row)


# Pattern: Open - Close
# Pattern: Start - Stop
# Pattern: Lock - Release
# Pattern: Change - Reset

# Generators and Context Managers
# The contextmanager Decorator
# contextlib.contextmanager
import contextlib


@contextlib.contextmanager
def open_file(fname):
    f = open(fname)
    try:
        yield f  # -> __enter__
    finally:
        f.close()  # -> __exit__


# Nested context
class NestedContext:
    def __init__(self) -> None:
        self._exits = []

    def __enter__(self):
        return self

    def enter_context(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in reversed(self._exits):
            exit(exc_type, exc_val, exc_tb)
        return False


# contextlib.ExitStack is like the NestedContext

f_names = [".gitignore", "main.py"]
with contextlib.ExitStack() as nc:
    files = [nc.enter_context(open(fname)) for fname in f_names]

    for f in files:
        print(f.read())
