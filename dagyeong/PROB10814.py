import sys

N = int(sys.stdin.readline().strip())
arr = []
index = 0
for _ in range(N):
    age, name = sys.stdin.readline().split()
    arr.append([int(age), index, name])
    index += 1

arr.sort()
for age, _, name in arr:
    print(age, name)