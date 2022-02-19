from collections import deque

q = deque()
q.appendleft(5)
q.append(7)
q.appendleft(8)
print(q)
# deque([8, 5, 7])


class Queue:
    def __init__(self) -> None:
        self.q = deque()

    def enqueue(self, val) -> None:
        self.q.appendleft(val)

    def dequeue(self) -> int:
        return self.q.pop()

    def is_empty(self) -> bool:
        return len(self.q) == 0

    def size(self) -> int:
        return len(self.q)


pq = Queue()
pq.enqueue(7)
pq.enqueue(8)
pq.enqueue(9)

print(pq.q)
# deque([9, 8, 7])

print(pq.dequeue())
# 7

print(pq.size())
# 2

print(pq.is_empty())
# False
