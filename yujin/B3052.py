#나머지
lst = []

for _ in range(10):
    i = int(input())
    lst.append(i % 42)

r = set(lst)
print(len(r))