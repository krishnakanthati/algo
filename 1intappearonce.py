a = [1, 1, 1, 2, 2, 2, 5, 5, 5, 9]

# checks if the sum of bits at a pos is multiple of 3
# if not multiple than add that (2 ** posofbit) to the ans
ans = 0

for i in range(0, 32):
    c = 0
    for j in a:
        if j & (1 << i):  # check the bit at ith pos
            c += 1

    if c % 3 == 1:  # remainder of total bits mod 3 is 1
        ans += (1 << i)

# print(ans)  # 9

ones, twos = 0, 0
for i in a:
    ones = (ones ^ i) & (~twos)
    twos = (twos ^ i) & (~ones)
# print(ones)  # 9


ones = 0
twos = 0

for i in a:
    twos = twos ^ (ones & i)
    ones = ones ^ i
    common_bit_mask = ~(ones & twos)
    ones &= common_bit_mask
    twos &= common_bit_mask
print(ones)  # 9
