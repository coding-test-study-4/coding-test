import sys

arr = [int(sys.stdin.readline()) for _ in range(9)]

MAX = max(arr)
print(MAX)
print(arr.index(MAX)+1)