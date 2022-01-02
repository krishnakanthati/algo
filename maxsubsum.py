# Maximum subarray sum brute force O(N^3)

a = [14, -11, 1, 12]
max = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        sum = 0
        for k in range(i, j+1):
            sum += a[k]
        if sum > max:
            max = sum

print(max)  # 16
