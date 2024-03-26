integer=[]

for i in range(10):
	remainder=int(input())%42	
	if remainder not in integer:
		integer.append(remainder)

print(len(integer))