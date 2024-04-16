import sys

# solution1: 브루트 포스가 뭐지? -> 근데 맞음,, 다 돌아보는게 브루트 포스인가?
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
MAX = 0

for i in range(len(lst)-2):
    for j in range(i+1, len(lst)-1):
        for k in range(j+1, len(lst)):
            sum = lst[i] + lst[j] + lst[k]
            if sum > MAX and sum <= M:
                MAX = sum

print(MAX)