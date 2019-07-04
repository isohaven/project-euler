
_sum = 0
a, b = 1, 2
while(True):
    if a > 4_000_000:
        break
    if a % 2 == 0:
        _sum += a
    a, b = b, a+b
print(_sum)
