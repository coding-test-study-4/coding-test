n=[]

while True:
  temp=int(input())
  if temp == -1:
    break
  n.append(temp)

a=[[]for i in range(len(n))]

for i in range(len(n)):
  for j in range(1, n[i]):
    if n[i]%j==0:
      a[i].append(j)

for i in range(len(n)):
  if sum(a[i])==n[i]:
    print(n[i], "=", end=" ")
    print(*a[i], sep=" + ")
  else:
    print(n[i], "is NOT perfect.", end=" ")
    print()
