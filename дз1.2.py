import cmath as cm
def solve (b, c):
    D = b ** 2 - 4 * c
    if - b - cm.sqrt(D) != 0:
        x1 = (-b - cm.sqrt(D)) / 2
        x2 = c / x1
    else:
        x1 = (-b + cm.sqrt(D)) / 2
        x2 = c / x1
    return x1, x2
