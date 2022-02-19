from collections import deque
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A', 'E', 'F'],
    'E': ['D', 'F', 'G'],
    'F': ['D', 'E', 'H'],
    'G': ['E', 'H'],
    'H': ['G', 'F']
}

v = set()
q = deque()


def bfs(node):
    v.add(node)
    q.appendleft(node)

    while q:
        m = q.pop()
        print(m, end=" ")
        for i in graph[m]:
            if i not in v:
                v.add(i)
                q.appendleft(i)


bfs('A')  # start node 'A'
# A B D C E F G H
