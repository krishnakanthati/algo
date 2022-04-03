import sys
sys.stdout = open("output.txt", 'w')
sys.stdin = open("input.txt", 'r')

# Dutch National Flag Algorithm
# 3 pointer -> low, mid, high

# Initially low and mid at start and high at the end

# [0.........low-1] -> 0's
# [low........high] -> 1's
# [high+1........n] -> 2's

# mid pointer can point either 1, 0 or 2
a = list(map(int, input().split()))
n = len(a)

l, h = 0, n-1
m = 0

while m <= h:
    if a[m] == 0:
        a[m], a[l] = a[l], a[m]
        m += 1
        l += 1
    elif a[m] == 1:
        m += 1
    elif a[m] == 2:
        a[m], a[h] = a[h], a[m]
        h -= 1
print(a)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
