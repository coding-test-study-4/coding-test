#수 정렬하기2
import sys

N = int(input())
lst = []

# 여러 줄을 한 번에 입력 받기
lst = [int(sys.stdin.readline()) for _ in range(N)]
# 한 번에 입력 안 받으면 시간 초과 뜸

lst.sort()

# 문자열로 출력을 한 번에 처리
# 출력도 for문 쓰지말고 한 번에
print('\n'.join(map(str, lst)))