string = input()
strings = set()

for i in range(len(string)):
    for j in range(i, len(string)):
        strings.add(string[i:j+1])

print(len(strings))
