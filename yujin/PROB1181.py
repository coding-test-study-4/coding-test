#단어 정렬
#sort는 좋은거구나,,,,

import sys
N = int(input())
lst = []

for i in range(N):
    lst.append(sys.stdin.readline().strip())

s_lst = set(lst)

lst = list(s_lst)
lst.sort()  
lst.sort(key = len)

for i in lst:
    print(i)