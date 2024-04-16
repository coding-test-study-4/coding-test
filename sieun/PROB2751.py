import sys

N = int(input())
numbers = []

# 수 범위가 클경우 그냥 int(input()) 을 사용하면 시간초과 남
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for i in range(N):
    print(numbers[i])
