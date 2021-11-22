def binary_search(a, k):
    left = 0
    right = len(a) -1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == k:
            return mid
        elif a[mid] > k:
            right = mid - 1
        elif a[mid] < k:
            left = mid + 1
    return False

a = [1, 2, 5, 7, 8]
k = 7
print(binary_search(a, k)) # 7 is present at index 3