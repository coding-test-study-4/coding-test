import sys

s = sys.stdin.readline().strip()
part_s = set()
for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        part_s.add(s[i:j])
        
print(len(part_s))