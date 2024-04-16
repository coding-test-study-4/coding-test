import sys

N = int(sys.stdin.readline().strip())
res = 0
for num in range(1, N):
    # 자릿수 합 구하기
    num_lst = [int(i) for i in str(num)]
    if N == (sum(num_lst) + num):
        res = num
        break
    
print(res)