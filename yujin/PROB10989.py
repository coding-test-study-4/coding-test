#수 정렬하기3

#메모리 초과
#input 대신 sys.stdin.readline()사용
import sys

N = int(sys.stdin.readline())

lst = [0] * 10001

for _ in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)