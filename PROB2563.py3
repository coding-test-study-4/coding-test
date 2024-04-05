# #3-색종이(2563)

N=int(input())

paper=[[0]*100 for i in range(100)]

for i in range(N):
  a,b=map(int,input().split())

  for y in range(a, a+10):
    for x in range(b, b+10):
      paper[x][y]=1

S=sum(paper,[])
print(sum(S))