import sys

def counting_sort(cnt_arr):
    for n in range(0, len(cnt_arr)):
        if cnt_arr[n] != 0:
            for _ in range(cnt_arr[n]): print(n)
            

N = int(sys.stdin.readline().strip())
cnt_arr = [0] * 10001
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    cnt_arr[n] += 1
counting_sort(cnt_arr)

# python 기본 정렬, 퀵정렬 -> 메모리 초과 (why? 주어진 값 8m,,)
# 계수정렬 -> 메모리 적게 듦