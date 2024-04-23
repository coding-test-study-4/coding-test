N = int(input())

words_set = set()
words = []

for i in range(N):
    words_set.add(input())
# print(words_set)

for word in words_set:
    words.append(word)
# print(words)

words.sort(key=lambda x:(len(x), x))
# print(words)

for word in words:
    print(word)
