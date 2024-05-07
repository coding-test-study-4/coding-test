import sys

N = int(sys.stdin.readline().strip())
sangeun = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

dic = {}
for num in sangeun:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for a in arr:
    res = dic.get(a)
    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')