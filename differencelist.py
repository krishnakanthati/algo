import time

a = [10, 5, 20, 40, 50, -5, 60, 40, 23, 1]
b = a.copy()
n = len(a)


def update(l, r, x):
    for i in range(l, r+1):
        a[i] += x
    return a


def difference_array(l, r, x):
    d = []
    for i in range(n):
        if i == 0:
            d.append(b[i])
        else:
            d.append(b[i]-b[i-1])
    d.append(0)
    d[l] = d[l] + x
    d[r+1] = d[r+1] - x
    for i in range(n):
        if i == 0:
            b[i] = d[i]
        else:
            b[i] = b[i-1] + d[i]
    return b


print("Without DA", update(0, 10, 10))
print()
print("With DA", difference_array(0, 10, 10))
