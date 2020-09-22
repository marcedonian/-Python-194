import numpy as np
def recur(n, a):
    if n == 0:
        return np.log(1/a + 1)
    return 1/n - a * recur(n - 1, a)
print(recur(25, 0.1))

def recur_rev(n,a):
    if n == 50:
        return 0
    return 1/a * (1/n - recur_rev(n + 1, a))
print(recur_rev(25, 10))
