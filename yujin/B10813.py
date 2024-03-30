#공 바꾸기
n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]

for i in range(m):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

for i in range(n):
    print(lst[i], end = " ")