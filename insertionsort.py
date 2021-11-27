def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j] 
            j -= 1
        a[j + 1] = key
    return a

a = [2, 5, 3, 6, 1]
print(insertion_sort(a)) #[1, 2, 3, 5, 6]
