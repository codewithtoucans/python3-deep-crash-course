# rational numbers
from fractions import Fraction

# help(Fraction)


# use + - * /
a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(numerator=1, denominator=4)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a + b + c)
print(a.numerator)
print(a.denominator)
print(float(a))
