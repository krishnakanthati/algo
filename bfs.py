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
p = {}
d = {}

for j in graph.keys():
    d[j] = 0
    p[j] = None


def bfs(start):
    v.add(start)
    q.appendleft(start)
    while q:
        m = q.pop()
        print(m, end=" ")
        for i in graph[m]:
            if i not in v:
                v.add(i)
                q.appendleft(i)
                p[i] = m
                d[i] = d[m] + 1


bfs('A')  # A B D C E F G H

print()

path = []
goal = 'G'
while goal:
    path.append(goal)
    goal = p[goal]

path.reverse()
print(*path)  # A D E G
