student=[]
for i in range(31):
	student.append(i)

student.remove(0)

for i in range(28):
	apply=int(input())
	student.remove(apply)

print(min(student))
print(max(student))