#대표값2
lst=[]
s = 0
for _ in range(5):
    lst.append(int(input()))

for i in range(len(lst)):
    s += lst[i-1]

lst.sort()
avg = s//5
#m = min(lst, key = lambda x : abs(x-avg)) 이건 근사값임

print(avg)
print(lst[2])