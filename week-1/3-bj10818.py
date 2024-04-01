import sys

sys.stdin.readline()
_min, _max = 1000001, -1000001
for i in map(int, sys.stdin.readline().split(' ')):
    if _max < i:    _max = i
    if _min > i:    _min = i
print(f"{_min} {_max}")