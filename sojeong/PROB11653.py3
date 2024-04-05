N=int(input())
a=[]
d=2

if N != 1:
  while N>1:
    while N%d==0:
      a.append(d)
      N//=d
    d+=1
  
  for i in range(len(a)):
    print(a[i])
