a = [2, 3, 4]

# total subsets equals 2 ** len(a) => 8
# 2 ** len(a) => 1 << len(a)

l = []

for num in range(2 ** len(a)):
    ds = []
    for bit in range(0, len(a)):
        if num & 1 << bit:
            ds.append(a[bit])
    l.append(ds)

print(l)  # [[], [2], [3], [2, 3], [4], [2, 4], [3, 4], [2, 3, 4]]
