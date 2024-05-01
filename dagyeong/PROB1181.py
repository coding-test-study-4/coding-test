import sys

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    arr.append([len(s), s])

arr.sort()
prev = ''
for num, val in arr:
    if prev == val: # 중복 제거
        continue
    print(val)
    prev = val