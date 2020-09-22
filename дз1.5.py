import math
def round_to_n(x, n):
    if x == 0:
        return x
    else:
        return round(x, -int(math.floor(math.log(abs(x)))) + (n - 1))
res = 0
for k in range(1, 3001):
    res = round_to_n(res + 1/k**2, 4)
print(res)
