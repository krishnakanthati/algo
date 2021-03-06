# Maximum subarray sum brute force O(N^3)

# a = [14, -11, 1, 12]
# max = 0
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         sum = 0
#         for k in range(i, j+1):
#             sum += a[k]
#         if sum > max:
#             max = sum

# print(max)  # 16

# Maximum subarray sum brute force O(N^2)

# a = [14, 11, -1, -12]
# max = 0
# for i in range(len(a)):
#     sum = 0
#     for j in range(i, len(a)):
#         sum += a[j]
#         if sum > max:
#             max = sum
# print(max) # 25


# Maximum subarray sum Kadane's Algorithm
# a = [-14, -11, 11, 12]

# max_ending_here = 0
# max_so_far = 0

# for i in range(len(a)):
#     max_ending_here += a[i]
#     if max_ending_here < 0:
#         max_ending_here = 0
#     max_so_far = max(max_so_far, max_ending_here)

# print(max_so_far) # 23
