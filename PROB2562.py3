a=[]
for i in range(9):
	a.append(int(input()))

num=max(a)
print(num)
print(a.index(num)+1)
