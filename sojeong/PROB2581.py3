M=int(input())
N=int(input())

a=[0]

for i in range(M, N+1):
  temp=0
  for j in range(1, i):
    if i%j==0:
      temp+=1
  if temp==1:
    a.append(i)

if sum(a)==0:
  print("-1")
else:
  a.remove(0)
  print(sum(a))
  print(min(a))
