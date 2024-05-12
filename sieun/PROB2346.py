from collections import deque

N = int(input())
papers = list(map(int, input().split()))
result = []

balloons = deque(range(1, N + 1))

while balloons:
    result.append(balloons.popleft())

    if balloons:
        step = papers[result[-1] - 1]

        if step > 0:
            balloons.rotate(-(step - 1))
        else:
            balloons.rotate(-step)

print(' '.join(map(str, result)))
