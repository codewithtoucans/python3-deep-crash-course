import math

# floats
x = 0.1 + 0.1 + 0.1
y = 0.3
print(format(x, ".25f"))
print(format(y, ".25f"))
print(x == y)
print(round(x, 5) == round(y, 5))

# flaot -> int  data loss
print(math.trunc(10.4))
print(math.trunc(10.5))
print(math.trunc(10.6))
print(math.trunc(-10.4))
print(math.trunc(-10.5))
print(math.trunc(-10.6))

print(math.floor(10.4))
print(math.floor(10.5))
print(math.floor(10.6))
print(math.floor(-10.4))
print(math.floor(-10.5))
print(math.floor(-10.6))

print(math.ceil(10.4))
print(math.ceil(10.5))
print(math.ceil(10.6))
print(math.ceil(-10.4))
print(math.ceil(-10.5))
print(math.ceil(-10.6))

# round will rounds to nearest value, with ties going to the nearest even value
print(round(1.25, 1))
print(round(1.35, 1))
print(round(-1.25, 1))
print(round(-1.35, 1))
