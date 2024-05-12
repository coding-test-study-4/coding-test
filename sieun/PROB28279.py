import sys
from collections import deque

N = int(sys.stdin.readline())
deque = deque()
for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))
    n = cmd[0]
    if n == 1:
        deque.appendleft(cmd[1])
    elif n == 2:
        deque.append(cmd[1])
    elif n == 3:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif n == 4:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif n == 5:
        print(len(deque))
    elif n == 6:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif n == 7:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif n == 8:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            