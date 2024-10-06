def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))
# 120


# from functools import lru_cache
# @lru_cache(maxsize=None)
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)

# print(factorial(5))
# 120
