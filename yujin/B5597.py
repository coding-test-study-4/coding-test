#과제 안 내신 분..?
lst = [i for i in range(1, 31)]

for _ in range(28):
    i = int(input())
    if i in lst:
        lst.remove(i)

print(min(lst))
print(max(lst))