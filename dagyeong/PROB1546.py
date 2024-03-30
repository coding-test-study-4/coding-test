import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

MAX = max(arr)
res = [val/MAX*100 for val in arr]
print(sum(res) / N)
