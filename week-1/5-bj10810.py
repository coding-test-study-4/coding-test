import sys

N, M = map(int, sys.stdin.readline().split(' '))

basket = [0 for i in range(N)]
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split(' '))
    for l in range(i-1, j): basket[l] = k

for n in basket:    print(n, end=' ')