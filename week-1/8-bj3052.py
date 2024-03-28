import sys

rems = []
for _ in range(10):
    rem = int(sys.stdin.readline()) % 42
    if rem not in rems:    rems.append(rem)
print(len(rems))