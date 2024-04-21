#좌표 압축
import sys
N = int(input())
lst = list(map(int,sys.stdin.readline().rstrip().split()))

s_lst = sorted(list(set(lst)))
d_lst = dict(zip(s_lst,list(range(len(s_lst)))))

for i in lst:
    print(d_lst[i])