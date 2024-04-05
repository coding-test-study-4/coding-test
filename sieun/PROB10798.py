words = [""] * 5
max_length = 0

for i in range(5):
    words[i] = input()
    if len(words[i]) > max_length:
        max_length = len(words[i])

result = ""
for i in range(max_length):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]

print(result)