#소트인사이드
import sys

N = int(sys.stdin.readline())
lst = list(map(int, str(N)))

lst.sort(reverse= True)

for i in lst:
    print(i, end="")