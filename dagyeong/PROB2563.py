import sys

n = int(sys.stdin.readline())
w_max = 0
h_max = 0
arr = []
for ___ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    w_max = max(w_max, w)
    h_max = max(h_max, h)
    arr.append([w, h])

res = [[0 for _ in range(w_max+10)] for __ in range(h_max+10)]
for lst in arr:
    for y in range(lst[0], lst[0]+10):
        for x in range(lst[1], lst[1]+10):
            res[x][y] = 1

s = 0
for r in res:
    s += sum(r)

print(s)