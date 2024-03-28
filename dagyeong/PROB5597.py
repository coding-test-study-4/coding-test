import sys

arr = [0 for _ in range(30)]

for _ in range(28):
    arr[int(sys.stdin.readline())-1] = 1

idx = arr.index(0) + 1
print(idx)
arr[idx-1] = 1
print(arr.index(0) + 1)