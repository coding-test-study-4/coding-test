import sys

res = set()

for _ in range(10):
    res.add(int(sys.stdin.readline()) % 42)

print(len(res))
