# petr and combination lock

a = [90, 265, 1, 1, 1, 1, 1]
n = len(a)

# total set is 2 ** n

flag = 0

for i in range(0, 2**n):
    ds = 0
    for bit in range(0, n):
        if i & (1 << bit):
            ds += a[bit]
        else:
            ds -= a[bit]
    if ds % 360 == 0:
        flag = 1
        print("YES")
        break

if not flag:
    print("NO")

# YES
