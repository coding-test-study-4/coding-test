import sys

N = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

res = 0
for n in range(N):
    res += int(s[n])

print(res)