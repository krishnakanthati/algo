a = [1, 1, 2, 2, 3, 3, 4, 5, 4, 7, 7, 9]


xor = 0

for i in a:
    xor ^= i

c = 0
while xor:
    if (xor & 1) == 1:
        break

    c += 1
    xor >>= 1

xor1, xor2 = 0, 0

for i in a:
    if i & (1 << c):
        xor1 ^= i
    else:
        xor2 ^= i


print(xor1, xor2)
