N=int(input())

a=list(map(int, input().split()))
b=[]
for i in range(N):
  temp=0
  for j in range(1, a[i]):
    if a[i]%j==0:
      temp+=1
  if temp == 1:
    b.append(a[i])

print(len(b))