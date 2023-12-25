a = [2, 3, 4]

# total subsets equals 2 ** len(a) => 8
# 2 ** len(a) => 1 << len(a)
# only use if n ~ 16|17|18
# TC: (2 ** len(a)) * n

l = []

for num in range(2 ** len(a)):
    ds = []
    for bit in range(0, len(a)):
        if num & 1 << bit:  # checks if the bit is set
            ds.append(a[bit])  # if the bit is set then appends the value to ds
    l.append(ds)

print(l)  # [[], [2], [3], [2, 3], [4], [2, 4], [3, 4], [2, 3, 4]]


"""
a: * 4 3 2
i: * 2 1 0
0: 0 0 0 1
1: 0 0 1 0
2: 0 0 1 1
3: 0 1 0 0
4: 0 1 0 1
5: 0 1 1 0
6: 0 1 1 1
7: 1 0 0 0
"""
