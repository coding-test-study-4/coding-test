import sys
import re

N = int(sys.stdin.readline().strip())
r = r'[012345789]'
cnt = 0
num = 665

while True:
    num += 1
# for num in range(666, 10001):
    res = re.sub(r, ',', str(num))
    for n in res.split(','):
        if len(n) >= 3:
            cnt += 1
            break
    if cnt == N:
        print(num)
        break