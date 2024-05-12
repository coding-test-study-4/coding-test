import sys

N, M = map(int, sys.stdin.readline().split())
people = {}
cnt = 0
res = []

for _ in range(N):
    name = sys.stdin.readline().strip()
    people[name] = 'h'
for _ in range(M):
    name = sys.stdin.readline().strip()
    try:
        if people[name] == 'h':
            cnt += 1
            res.append(name)
    except:
        continue

print(cnt)
print(*sorted(res), sep='\n')