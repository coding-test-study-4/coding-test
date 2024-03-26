N, M=map(int, input().split())
basket=[]

for i in range(N+1):
	basket.append(i)

for a in range(M):
	i, j=map(int, input().split())
	ball=basket[i]
	basket[i]=basket[j]
	basket[j]=ball

for a in range(1, N+1):
	print(basket[a], end=" ")