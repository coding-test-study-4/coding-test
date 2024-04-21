#좌표 정렬하기 2
import sys
N = int(input())

lst = []

for _ in range(N):
    [a,b] = map(int, sys.stdin.readline().split())
    lst.append([a,b])

lst.sort(key=lambda x:(x[1], x[0]))

for i in lst:
    print(i[0], i[1])
