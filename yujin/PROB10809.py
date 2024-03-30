#알파벳 찾기
S = input()
a = 'abcdefghijklmnopqrstuvwxyz'
r = []
for i in a:
    if i in S:
        print(S.index(i), end=" ")
    if i not in S:
        print(-1, end=" ")