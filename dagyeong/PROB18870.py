import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr_dic = {v:k for k, v in enumerate(sorted(list(set(arr))))}

for val in arr:
    print(arr_dic.get(val), end=' ')