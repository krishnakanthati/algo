def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

arr = [5, 4, 3, 2, 1]

bubble_sort(arr)
print(*arr)

# 1 2 3 4 5
