import sys

N, M = map(int, sys.stdin.readline().split())
dic = {val:0 for val in list(sys.stdin.readline().strip() for _ in range(N))}
check = list(sys.stdin.readline().strip() for _ in range(M))

for s in check:
    if s in dic.keys():
        dic[s] += 1

print(sum(dic.values()))