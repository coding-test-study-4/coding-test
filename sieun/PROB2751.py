import sys

n = int(input())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

# 그냥 정렬하면 메모리 초과 남
for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
