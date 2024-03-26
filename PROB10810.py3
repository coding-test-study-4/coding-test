N, M=map(int, input().split())
basket=[0 for i in range(N+1)]

for a in range(M):
	i, j, k=map(int, input().split())
	for b in range(i, j+1):
		basket[b]=k

for a in range(1, N+1):
	print(basket[a], end=" ")
