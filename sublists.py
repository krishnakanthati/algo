# sublist from a given list

def sub_lists(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists

print(sub_lists([1, 2, 3]))

# [[1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]