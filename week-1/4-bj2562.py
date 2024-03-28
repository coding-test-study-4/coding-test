import sys

_max, _argmax = 0, -1
for i in range(1, 10):
    n = int(sys.stdin.readline())
    if _max < n: _max, _argmax = n, i
print(f"{_max}\n{_argmax}")