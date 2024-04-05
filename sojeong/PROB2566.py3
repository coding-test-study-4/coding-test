# #3-최댓값(2566)

A=[list(map(int, input().split())) for i in range(9)]

M=max(map(max, A))

B=[[i,j] for i in range(9) for j in range(9) if A[i][j]==M]

print(M)
print(B[0][0]+1, B[0][1]+1, end=" ")
