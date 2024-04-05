# #3-세로읽기(10798)

A=[list(map(str, input())) for i in range(5)]
B=[]

for i in range(15):
   for j in range(len(A)):
    if i<len(A[j]):
      B.append(A[j][i])

print(*B, sep="")