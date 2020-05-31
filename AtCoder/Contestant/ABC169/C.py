from decimal import Decimal, ROUND_DOWN

marume = 1
a, b = map(str, input().split())
print((Decimal(a) * Decimal(b)).quantize(Decimal(marume), rounding=ROUND_DOWN))
