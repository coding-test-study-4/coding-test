N, M=map(int, input().split())
basket=[]

for i in range(N+1):
	basket.append(i)
basket.remove(0)

for a in range(M):
	i, j=map(int, input().split())
	number=basket[i-1:j]
	number.reverse()
	basket[i-1:j]=number

for a in range(N):
	print(basket[a], end=" ")
