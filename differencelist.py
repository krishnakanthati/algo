a = [10, 5, 20, 40]
b = [10, 5, 20, 40]


def update(l, r, x):
    for i in range(l, r+1):
        a[i] += x
    return a


def difference_array(l, r, x):
    d = []
    for i in range(len(b)):
        if i == 0:
            d.append(b[i])
        else:
            d.append(b[i]-b[i-1])
    d[l] = d[l] + x
    d[r+1] = d[r+1] - x
    for i in range(len(b)):
        if i == 0:
            b[i] = d[i]
            res = d[i]
        else:
            res += d[i]
            b[i] = res
    return b


print(update(0, 1, 10))
print(difference_array(0, 1, 10))
