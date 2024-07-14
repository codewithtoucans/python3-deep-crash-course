# decimals
from decimal import Decimal
import decimal

a = Decimal("1.25")
b = Decimal("1.25")

# decimal.getcontext().prec = 6
print(decimal.getcontext())
print(round(a, 1))

with decimal.localcontext() as ctx:
    ctx.prec = 10
    ctx.rounding = decimal.ROUND_UP
    print(round(b, 1))
    print(ctx)


print(Decimal(0.1) == Decimal("0.1"))
print(Decimal(10) == Decimal("10"))

# use math operators
print(Decimal(1) / Decimal(3))

# use + - * /
print(Decimal(1) + Decimal(3))
print(Decimal(1) - Decimal(3))
print(Decimal(1) * Decimal(3))
print(Decimal(1) / Decimal(3))

# use ** power
print(Decimal(1) ** Decimal(3))

# use floor
print(Decimal(1) // Decimal(3))

# use modulo
print(Decimal(1) % Decimal(3))

# use divmod
print(divmod(Decimal("101"), Decimal("5")))
print(Decimal("101").sqrt())
