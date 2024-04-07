#약수 구하기
rs = []
N, k = map(int, input().split())

for i in range(1, N+1):
    if(N%i==0):
        rs.append(i)

if(len(rs)<k):
    print(0)
else:
    print(rs[k-1])