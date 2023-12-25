a = [1, 1, 1, 2, 2, 2, 4, 4, 4, 7, 7, 7, 6, 6, 6, 5]
ans = 0

for i in range(0, 32):
    c = 0
    for j in a:
        if j & (1 << i):
            c += 1

    if c % 3 == 1:
        ans += 2 ** i

print(ans)
