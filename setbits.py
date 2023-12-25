# traditional way
# 107 1101011

n = 107

c = 0
while n != 0:
    if n % 2 != 0:  # check if the number is odd
        c += 1
    n //= 2

# print(c)  # 5


# O(MSB)
n = 107
c = 0

while n != 0:
    if n & 1 == 1:  # check if the number is odd
        c += 1
    n >>= 1

# print(c)  # 5


# O(Set Bit)
n = 107
c = 0

while n != 0:
    n &= n-1  # count the last set bit & turns it off
    c += 1
    n >>= 1

print(c)  # 5
