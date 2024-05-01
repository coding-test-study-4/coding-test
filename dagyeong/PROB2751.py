import sys

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = sorted(arr)
print(*res, sep='\n')

# 선택정렬, 버블정렬 -> 시간초과
# 퀵정렬 -> 메모리초과
# ???