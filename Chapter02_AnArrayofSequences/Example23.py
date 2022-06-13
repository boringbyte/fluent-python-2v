from collections import deque


dq = deque(range(10), maxlen=10)
dq
dq.rotate(3)
dq
dq.rotate(-4)
dq
dq.appendleft(-1)
dq
dq.extend([11, 22, 33])
dq
dq.extendleft([10, 20, 30, 40])
dq
